import socket, select, string, sys

from etc import standard

class Client(object):

	def __init__(self, conn):
		self.conn = conn

	def send(self, data):
		self.conn.send(data)

	def login(self, username):
		param = {}
		param[standard.PARAM_USERNAME] = username

		data = {}
		data[standard.MESSAGE] = MESSAGE_AUTH
		data[standard.MESSAGE_PARAM] = param
		self.conn.send(data)

"""
def initPrompt() :
		sys.stdout.write('You > ')
		sys.stdout.flush()

if __name__ == "__main__":

	if (len(sys.argv) < 3):
		print "Usage: python client.py <hostname> <port>"
		sys.exit()

	host = sys.argv[1]
	port = sys.argv[2]
	RECV_BUF = 4096

	# Create a TCP/IP Socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(2)

	try:
		sock.connect( (host, int(port)) )
	except :
		print "Unable to connect to %s:%s" %(host,port)
		sys.exit()

	print "Connected to remote host. Start sending messages!"
	initPrompt()

	username = raw_input("Username = ")

	data = {
		"message" 	: "auth"
		"param" 	: {
			"username"	: username
		}
	}

	msg = json.dumps(data)

	sock.sendall(msg)

	while 1:
		socket_list = [sys.stdin, sock]		# the list of socket descriptors

		#get the list socket
		readsock, writesock, errsock = select.select(socket_list, [], [])

		for sock in readsock:
			#incoming messages
			if (sock == sock):
				data = sock.recv(RECV_BUF)
				if (data):
					sys.stdout.write(data)
					initPrompt()
				else :
					print "\nDisconnected from server!"
					sys.exit()

			else:
				# client send message
				msg = sys.stdin.readline()
				sock.send(msg)
"""