import socket, select, string, sys

import standard

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
		print data
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

	def onlinePlayers(self):
		data = {}
		data[standard.MESSAGE] = "list_user"
		self.send(data)

	def joinRoom(self, roomId, playerId):
		param = {}
		param[standard.PARAM_ROOM_Id] = roomId
		param[standard.PARAM_PLAYER_Id] = playerId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def joinGame(self, playerId, roomId):
		param = {}
		param[standard.PARAM_PLAYER_Id] = playerId
		param[standard.PARAM_ROOM_Id] = roomId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def setPawn(self, row, col, playerId):
		param = {}
		param[standard.PARAM_ROW] = row
		param[standard.PARAM_COL] = col
		param[standard.PARAM_PLAYER_Id] = playerId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_SET_PAWN
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def spectate(self, roomId):
		param = {}
		param[standard.PARAM_ROOM_Id] = roomId

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

	def handler(self):
		while 1:
			try:
				socket_list = [sys.stdin, self.conn.socket]
				readsock, writesock, errsock = select.select(socket_list, [], [])

				for sock in readsock:
					#incoming messages
					if (sock == self.conn.getSocket()):
						data = self.conn.recv()
						if standard.MESSAGE in data:
							if data[standard.MESSAGE] == standard.MESSAGE_AUTH:
								if data[standard.MESSAGE_SUCCESS] == 1:
									print "login successful. your login key =", data["player_id"]
								else:
									print "login unsuccessful..."
							elif data[standard.MESSAGE] == standard.MESSAGE_REFRESH:
								for room in data["room_list"]:
									print room
							elif data[standard.MESSAGE] == standard.MESSAGE_CREATE_ROOM:
								if data[standard.MESSAGE_SUCCESS] == 1:
									print "create room successful."
								else:
									print "create room unsuccessful..."
							elif data[standard.MESSAGE] == "list_user":
								for player in data["player_list"]:
									print player
						else :
							print "\nDisconnected from server!"
							sys.exit()

					else:
						# client send message
						msg = sys.stdin.readline()
						command = msg.split()

						if (command[0] == standard.MESSAGE_AUTH):
							self.login(command[1])
						elif (command[0] == standard.MESSAGE_REFRESH):
							self.refresh()
						elif (command[0] == standard.MESSAGE_CREATE_ROOM):
							self.createRoom(command[1])
						elif (command[0] == "online"):
							self.onlinePlayers()
			except Exception, e:
				print e

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