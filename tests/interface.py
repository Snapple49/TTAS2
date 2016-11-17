import telnetlib

host = "sid.cs.ru.nl"
port = 25999

tn = telnetlib.Telnet(host, port)

def sign_on(id, password):
	tn.write('signon %s:%s\n' % (id,password)) 

def sign_off():
	tn.write('signoff\n')

def get_variable(variable):
	tn.write('get %s\n' % variable)

def art_id(barcode):
	tn.write('artid %s\n' % barcode)

def art_reg(barcode, amount=1):
	tn.write('artreg %s:%s\n' % (barcode, amount))

def trans(method, amount=""):
	tn.write('trans %s %s\n' % (method, amount))

def idle():
	tn.write('idle\n')

def quit():
	tn.write('quit\n')

def open_acc(acc=""):
	tn.write('open %s\n' % acc)

def close_acc():
	tn.write('close\n')

def flush():
	print (tn.read_all())