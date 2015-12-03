from GameController import *
from MessageController import *

import socket, select, json

class Server(object):
	"""docstring for Server"""
	def __init__(self, address="0.0.0.0", port=5000):
		super(Server, self).__init__()
		self.CONNECTION_LIST = []	# list of socket client connected
		self.port = port 
		self.ipaddr = address

		# create a new socket
		self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sockfd.bind((self.ipaddr, self.port))
		self.sockfd.listen(5)

		self.CONNECTION_LIST.append(servsock)

		self.gameServer = GameController()
		self.msServer = MessageController()
		print "Game server started on port " + str(self.port)

	def serverListen(self):
		while 1:
			readsock, writesock, errsock = select.select(CONNECTION_LIST, [], [])

			for sock in readsock:
				if sock == self.sockfd:
					sockfd, addr = self.sockfd.accept()
					self.CONNECTION_LIST.append(sockfd)
					print "Client %s:%s connected" % addr

				else:
					try:
						msg = self.msServer.receiveMessage(sock)	# receive the message sent from sock
						msgType = msg["message"]

						if msgType == "auth":						# user first-time log into the server
							playerName = msg["params"]["name"]
							player = self.gameServer.newPlayer(playername, sock)
							self.gameServer.addPlayerOnline(player)

							obj = dict([("message", msgType), ("success", 1), ("player_id", player.getPlayerId())])
							print obj
							self.msServer.sendMessage(sock, obj)

						elif msgType == "refresh":				# get the list of the room in the server
							roomList = []
							for room in self.gameServer.getRoomList():
								roomTuple = [("id", room.getRoomId()), ("name", room.getRoomName())]
								roomList.append(roomTuple)

							obj = dict([("message", msgType), ("success", 1), ("room_list", roomList)])
							self.msServer.sendMessage(sock, obj)

						elif msgType == "create_room":			# player want to create a new room with the name
							roomName = msg["params"]["name"]
							room = self.gameServer.newRoom(roomName)
							self.gameServer.addRoom(room)

							obj = dict([("message", msgType), ("success", 1)])
							self.msServer.sendMessage(sock, obj)

						elif msgType == "join_room":			# player want to join the defined room
							roomId = msg["params"]["room_id"]
							roomTarget = self.gameServer.getRoomList()[roomId]

							# check if the room is full
							# if not full, add the player to the room
							if len(roomTarget.getPlayersInRoom()) < 5:
								roomTarget.addPlayerToRoom(msg["params"]["player_id"])
								obj = dict([("message", msgType), ("success", 1)])
							else:
								obj = dict([("message", msgType), ("success", 0)])
								
							self.msServer.sendMessage(sock, obj)

						elif msgType == "left_room":			# case if the player lefts the current room he was in
							roomId = msg["params"]["room_id"]
							roomTarget = self.gameServer.getRoomList()[roomId]

							roomTarget.deletePlayerFromRoom(msg["params"]["player_id"])
							if len(roomTarget.getPlayersInRoom()) == 0:
								# function to delete the room
								gameServer.deleteRoom(roomTarget)
								print "Room %d deleted! Room is empty" % (roomId)

							obj = dict([("message", msgType), ("success", 1)])
							self.msServer.sendMessage(sock, obj)

						else:
							pass


					except Exception, e:
						if sock in self.CONNECTION_LIST:
							self.CONNECTION_LIST.remove(sock)
						print "Client (%s, %s) is offline!" % addr
						
						sock.close()
						
						continue

	def close(self):
		self.sockfd.close()


		