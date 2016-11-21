import re
import telnetlib

host = "sid.cs.ru.nl"
port = 25999
debug = True
tn = telnetlib.Telnet(host, port)

def run_command(command, lines=1):
	tn.write(command)
	response = flush_lines(lines)
	if debug:
		print(command)
		print(response)
	return response

def sign_on(id, password):
	command = 'signon %s:%s\n' % (id,password)
	return run_command(command)

def sign_off():
	command = 'signoff\n' 
	return run_command(command)

def get_variable(variable):
	command = 'get %s\n' % variable
	return run_command(command)

def art_id(barcode):
	command = 'artid %s\n' % barcode
	return run_command(command)

def art_reg(barcode, amount=1):
	command = 'artreg %s:%s\n' % (barcode, amount)
	# ARTEREG returns 2 lines so we need to flush 2 lines
	return run_command(command, 2)
	
def art_reg_empty():
	command = 'artreg\n'
	# ARTEREG returns 2 lines so we need to flush 2 lines
	return run_command(command, 2)
	

def trans(method, amount=None, cents=None):
	if amount:
		cents =  cents or 0
		command = 'trans %s:%s,%s\n' % (method, amount, cents)
	else:
		command = 'trans %s\n' % (method)
	return run_command(command)

def idle():
	command = 'idle\n'
	return run_command(command)

def open_acc(acc=""):
	command = 'open %s\n' % acc
	return run_command(command)

def close_acc():
	command = 'close\n'
	return run_command(command)

def acc_state():
	return get_variable('CS_ACCNT')

def quit():
	command = 'quit\n'
	return run_command(command)

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





