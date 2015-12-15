from GameController import *
from MessageController import *

import standard
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

		self.CONNECTION_LIST.append(self.sockfd)

		self.gameServer = GameController()
		self.msServer = MessageController()
		print "Game server started on port " + str(self.port)

	def serverListen(self):
		while 1:
			readsock, writesock, errsock = select.select(self.CONNECTION_LIST, [], [])

			for sock in readsock:
				if sock == self.sockfd:
					sockfd, addr = self.sockfd.accept()
					self.CONNECTION_LIST.append(sockfd)
					print "Client %s:%s connected" % addr

				else:
					try:
						msg = self.msServer.receiveMessage(sock)	# receive the message sent from sock
						msgType = msg[standard.MESSAGE]

						if msgType == standard.MESSAGE_AUTH:						# user first-time log into the server
							playerName = msg[standard.MESSAGE_PARAM][standard.PARAM_USERNAME]
							player = self.gameServer.newPlayer(playerName, sock)
							self.gameServer.addPlayerOnline(player)

							obj = dict([(standard.MESSAGE, msgType), (standard.MESSAGE_SUCCESS, 1), ("player_id", player.getPlayerId())])
							print obj
							self.msServer.sendMessage(sock, obj)

						elif msgType == standard.MESSAGE_REFRESH:				# get the list of the room in the server
							roomList = []
							for room in self.gameServer.getRoomList():
								roomTuple = [("id", room.getRoomId()), ("name", room.getRoomName())]
								roomList.append(roomTuple)

							obj = dict([(standard.MESSAGE, msgType), (standard.MESSAGE_SUCCESS, 1), ("room_list", roomList)])
							self.msServer.sendMessage(sock, obj)

						elif msgType == standard.MESSAGE_CREATE_ROOM:			# player want to create a new room with the name
							roomName = msg[standard.MESSAGE_PARAM]["name"]
							room = self.gameServer.newRoom(roomName)
							self.gameServer.addRoom(room)

							obj = dict([(standard.MESSAGE, msgType), (standard.MESSAGE_SUCCESS, 1)])
							self.msServer.sendMessage(sock, obj)

						elif msgType == standard.JOIN_ROOM:			# player want to join the defined room
							roomId = msg[standard.MESSAGE_PARAM]["room_id"]
							roomTarget = self.gameServer.getRoomList()[roomId]

							# check if the room is full
							# if not full, add the player to the room
							if len(roomTarget.getPlayersInRoom()) < 5:
								roomTarget.addPlayerToRoom(msg[standard.MESSAGE_PARAM]["player_id"])
								obj = dict([(standard.MESSAGE, msgType), (standard.MESSAGE_SUCCESS, 1)])
							else:
								obj = dict([(standard.MESSAGE, msgType), (standard.MESSAGE_SUCCESS, 0)])
								
							self.msServer.sendMessage(sock, obj)

						elif msgType == standard.MESSAGE_LEAVE:			# case if the player lefts the current room he was in
							roomId = msg[standard.MESSAGE_PARAM]["room_id"]
							roomTarget = self.gameServer.getRoomList()[roomId]

							roomTarget.deletePlayerFromRoom(msg[standard.MESSAGE_PARAM]["player_id"])
							if len(roomTarget.getPlayersInRoom()) == 0:
								# function to delete the room
								gameServer.deleteRoom(roomTarget)
								print "Room %d deleted! Room is empty" % (roomId)

							obj = dict([(standard.MESSAGE, msgType), (standard.MESSAGE_SUCCESS, 1)])
							self.msServer.sendMessage(sock, obj)

						elif msgType == standard.MESSAGE_START_GAME:		# start the game command
							# check the current enlisted game if maximum
							

						else:
							pass


					except Exception, e:
						print e
						if sock in self.CONNECTION_LIST:
							self.CONNECTION_LIST.remove(sock)
						print "Client (%s, %s) is offline!" % addr
						
						sock.close()
						
						continue

					except KeyboardInterrupt:
						exit()

	def close(self):
		self.sockfd.close()


		