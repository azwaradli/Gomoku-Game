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
		param[standard.PARAM_ROOM_ID] = roomId
		param[standard.PARAM_PLAYER_ID] = playerId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def joinGame(self, playerId, roomId):
		param = {}
		param[standard.PARAM_PLAYER_ID] = playerId
		param[standard.PARAM_ROOM_ID] = roomId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_GAME
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def setPawn(self, row, col, playerId):
		param = {}
		param[standard.PARAM_ROW] = row
		param[standard.PARAM_COL] = col
		param[standard.PARAM_PLAYER_ID] = playerId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_SET_PAWN
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def spectate(self, roomId):
		param = {}
		param[standard.PARAM_ROOM_ID] = roomId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_JOIN_ROOM
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def leave(self, roomId, playerId):
		param = {}
		param[standard.PARAM_ROOM_ID] = roomId
		param[standard.PARAM_PLAYER_ID] = playerId

		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_LEAVE
		data[standard.MESSAGE_PARAM] = param
		self.send(data)

	def exit(self):
		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_EXIT
		self.send(data)
		self.conn.close()

	def startgame(self):
		data = {}
		data[standard.MESSAGE] = standard.MESSAGE_START_GAME
		self.send(data)

	"""
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
									self.player_id = data[standard.PARAM_PLAYER_ID]
									print "login successful. your login key =", self.player_id
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

							elif data[standard.MESSAGE] == standard.MESSAGE_JOIN_ROOM:
								if data[standard.MESSAGE_SUCCESS] == 1:
									self.room_id = data[standard.PARAM_ROOM_ID]
									print "you are connected to room", self.room_id
								else:
									print "login unsuccessful..."

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
						elif (command[0] == standard.MESSAGE_JOIN_ROOM):
							self.joinRoom(self.player_id, int(command[1]))
			except Exception, e:
				print e """
