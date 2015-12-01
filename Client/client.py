import socket, select, string, sys

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

	connsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connsock.settimeout(2)

	try:
		connsock.connect( (host, int(port)) )
	except :
		print "Unable to connect to %s:%s" %(host,port)
		sys.exit()

	print "Connected to remote host. Start sending messages!"
	initPrompt()

	while 1:
		socket_list = [sys.stdin, connsock]		#the list of socket descriptors

		#get the list socket
		readsock, writesock, errsock = select.select(socket_list, [], [])

		for sock in readsock:
			#incoming messages
			if (sock == connsock):
				data = sock.recv(RECV_BUF)
				if (data):
					sys.stdout.write(data)
					initPrompt()
				else :
					print "\nDisconnected from server!"
					sys.exit()

			else:
				#client send message
				msg = sys.stdin.readline()
				connsock.send(msg)