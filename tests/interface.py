import telnetlib

host = "sid.cs.ru.nl"
port = 25999

tn = telnetlib.Telnet(host, port)

def sign_on(id, password):
	tn.write('signon %s:%s\n' % (id,password)) 
	return flush_line()

def sign_off():
	tn.write('signoff\n')
	return flush_line()

def get_variable(variable):
	tn.write('get %s\n' % variable)
	return flush_line()

def art_id(barcode):
	tn.write('artid %s\n' % barcode)
	return flush_line()

def art_reg(barcode, amount=1):
	tn.write('artreg %s:%s\n' % (barcode, amount))
	return flush_line()

def trans(method, amount=""):
	tn.write('trans %s %s\n' % (method, amount))
	return flush_line()

def idle():
	tn.write('idle\n')
	return flush_line()

def open_acc(acc=""):
	tn.write('open %s\n' % acc)
	return flush_line()

def close_acc():
	tn.write('close\n')
	return flush_line()

def acc_state():
	return get_variable('CS_ACCNT')

def quit():
	tn.write('quit\n')

def flush_line():
	return tn.read_until('\n',2)

def flush():
	return tn.read_all()





