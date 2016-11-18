import re
import unittest
import interface as i

# Some helper methods to avoid repeating yourself (DRY!)
def up_to_close():
	i.open_acc()
	return i.close_acc()

def up_to_trans(method='TM_BANK'):
	up_to_close()
	return i.trans(method)

def up_to_idle():
	up_to_trans()
	return i.idle()

class BaseTestCase(unittest.TestCase):

	def setUp(self):
		i.flush_lines()
		i.sign_on(8,"01")

	def tearDown(self):
		i.sign_off()


class OpenedAccountTestCase(BaseTestCase):

	def setUp(self):
		super(OpenedAccountTestCase, self).setUp()
		i.open_acc()

	def tearDown(self):
		i.close_acc()
		i.trans('TM_BANK')
		i.idle()
		super(OpenedAccountTestCase, self).tearDown()

class GetVariableTestCase(BaseTestCase):

	# Test 1
	def test_pc_sfu(self):
		variable = i.get_variable('PC_SFU')
		return self.assertEqual(variable, "120 PC_SFU:0\n")

	# Test 2 
	def test_si_scrp(self):
		variable = i.get_variable('SI_SCRP')
		return self.assertEqual(variable, "210 SI_SCRP:2.1\n")

class AccountTestCase(BaseTestCase):

	def tearDown(self):
		i.close_acc()
		i.trans('TM_BANK')
		i.idle()
		super(AccountTestCase, self).tearDown()

	# Test 3
	def test_open_acc(self):
		rgx = re.compile(r"231 ([0-9])+ Account opened")
		response = i.open_acc()
		return self.assertIsNotNone(rgx.match(response))

	# Test 4
	def test_close_account(self):
		rgx = re.compile(r"230 [0-9]{1,},[0-9]{2,} Account closed")
		response = up_to_close()
		return self.assertIsNotNone(rgx.match(response))

	# Test 5
	def test_trans(self):
		rgx = re.compile(r"240 [0-9]{1,},[0-9]{2,} Transaction succeeded")
		response = up_to_trans('TM_BANK')
		return self.assertIsNotNone(rgx.match(response))

	# Test 6
	def test_idle(self):
		expected = "233 Account Idled\n"
		response = up_to_idle()
		return self.assertEqual(expected, response)

	# Test 7
	def test_invalid_trans(self):
		expected = "531 Invalid account state\n"
		i.open_acc()
		response = i.trans('TM_BANK')
		return self.assertEqual(expected, response)

	# Test 8
	def test_invalid_open(self):
		expected = "531 Invalid account state\n"
		i.open_acc()
		response = i.open_acc()
		return self.assertEqual(expected, response)

	# Test 9
	def test_invalid_idle(self):
		expected = "531 Invalid account state\n"
		up_to_close()
		response = i.idle()
		return self.assertEqual(expected, response)


class TransactionsTestCase(OpenedAccountTestCase):
	
	def test_valid_mthd(self):
		i.close_acc()
		response = i.trans('TM_BANK')
		return self.assertEqual(response, "240 0,00 Transaction succeeded\n")

class ArtRegTestCase(OpenedAccountTestCase):

	# Test 16
	def test_no_amount(self):
		expected = "212 Multifilter kek:6,99\n232 1: 6,99 Article registered\n"
		response = i.art_reg(59922827) 
		return (self.assertEqual(expected, response))  

	# Test 17
	def test_with_amount(self):
		expected = "212 Multifilter kek:20,97:3\n232 3: 20,97 Article registered\n"
		response = i.art_reg(59922827, 3)
		return (self.assertEqual(expected, response))

	# Test 18
	def test_neg_amount(self):
		expected = "501 Syntax error\n"
		response = i.art_reg(59922827, -2)
		return (self.assertEqual(expected, response))

	# Test 19
	def test_float_amont(self):
		expected = "501 Syntax error\n"
		response = i.art_reg(59922827, 2.45)
		return (self.assertEqual(expected, response))

	# Test 20
	def test_float_amont(self):
		expected = "501 Syntax error\n"
		response = i.art_reg(59922827, 0)
		return (self.assertEqual(expected, response))



