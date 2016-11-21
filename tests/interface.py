import re
import telnetlib

host = "sid.cs.ru.nl"
port = 25999

tn = telnetlib.Telnet(host, port)

def sign_on(id, password):
	tn.write('signon %s:%s\n' % (id,password)) 
	return flush_lines()

def sign_off():
	tn.write('signoff\n')
	return flush_lines()

def get_variable(variable):
	tn.write('get %s\n' % variable)
	return flush_lines()

def art_id(barcode):
	tn.write('artid %s\n' % barcode)
	return flush_lines()

def art_reg(barcode, amount=1):
	tn.write('artreg %s:%s\n' % (barcode, amount))
	# ARTEREG returns 2 lines so we need to flush 2 lines
	return flush_lines(2)
	
def art_reg_empty():
	tn.write('artreg\n')
	# ARTEREG returns 2 lines so we need to flush 2 lines
	return flush_lines(2)
	

def trans(method, amount=""):
	tn.write('trans %s:%s\n' % (method, amount))
	return flush_lines()

def idle():
	tn.write('idle\n')
	return flush_lines()

def open_acc(acc=""):
	tn.write('open %s\n' % acc)
	return flush_lines()

def close_acc():
	tn.write('close\n')
	return flush_lines()

def acc_state():
	return get_variable('CS_ACCNT')

def quit():
	tn.write('quit\n')

def flush_lines(l = 1):
	"""
	Tries to flush l lines and returns the response
	If the ReGex doesn't match, it returns the text received 
	so far. 
	"""
	rgx = re.compile(r'(?:.+\n){%s}' % l)
	(_, _, response) = tn.expect([rgx], 2)
	return response

def flush_all():
	"""
	Read everything until EOF. Blocks I/O until EOF is found.
	"""
	return tn.read_all()





