import unittest
import interface as i

class BaseTestCase(unittest.TestCase):

	def setUp(self):
		i.flush_line()
		i.sign_on(8,"01")

	def tearDown(self):
		#i.quit()
		pass


class OpenedAccountTestCase(BaseTestCase):
	
	def setUp(self):
		super().setUp()
		i.open_acc()

	def tearDown(self):
		i.close_acc()
		super().quit()

class GetVariableTestCase(BaseTestCase):

	def test_si_scrp(self):
		variable = i.get_variable('SI_SCRP')
		return self.assertEqual(variable, "210 SI_SCRP:2.1\n")

	def test_pc_sfu(self):
		variable = i.get_variable('PC_SFU')
		return self.assertEqual(variable, "120 PC_SFU:0\n")

class TransactionsTestCase(OpenedAccountTestCase):
	
	def test_valid_mthd(self):
		i.close_acc()
		response = i.trans('TM_BANK')
		return self.assertEqual(response, "240 0,00 Transaction succeeded\n")
		
		
		
		
		
		
		
		
		
		
		
		
		
		