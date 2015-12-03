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
		data[standard.MESSAGE] = standard.MESSAGE_AUTH
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def createRoom(self, roomName):
		param = {}
		param[standard.PARAM_ROOM_NAME] = roomName

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_CREATE_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def refresh(self):
		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_REFRESH
		self.send(data)

	def joinRoom(self, roomID, playerID):
		param = {}
		param[standard.PARAM_ROOM_ID] = roomID
		param[standard.PARAM_PLAYER_ID] = playerID

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def joinGame(self, playerID, roomID):
		param = {}
		param[standard.PARAM_PLAYER_ID] = playerID
		param[standard.PARAM_ROOM_ID] = roomID

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def setPawn(self, row, col, playerID):
		param = {}
		param[standard.PARAM_ROW] = row
		param[standard.PARAM_COL] = col
		param[standard.PARAM_PLAYER_ID] = playerID

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_SET_PAWN
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def spectate(self, roomID):
		param = {}
		param[standard.PARAM_ROOM_ID] = roomID

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def leave(self):
		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_LEAVE
		self.send(data)

	def exit(self):
		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_EXIT
		self.send(data)
		self.conn.close()


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