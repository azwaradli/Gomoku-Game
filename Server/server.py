from GameController import *
from MessageController import *

import socket, select, json

def broadcast_data(sock, message):
	for socket in CONNECTION_LIST:
		if socket != servsock:
			try:
				socket.send(message)
			except :
				socket.close()
				CONNECTION_LIST.remove(sock)


if __name__ == "__main__":

	CONNECTION_LIST = []	# list of socket client connected
	RECV_BUF = 4096
	PORT = 5000
	IP_ADDR = "0.0.0.0"

	servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	servsock.bind((IP_ADDR, PORT))
	servsock.listen(10)

	CONNECTION_LIST.append(servsock)

	gameServer = GameController()
	msServer = MessageController()
	print "Game server started on port " + str(PORT)

	while 1:
		readsock, writesock, errsock = select.select(CONNECTION_LIST, [], [])

		for sock in readsock:
			if sock == servsock:
				sockfd, addr = servsock.accept()		# accept the connection
				CONNECTION_LIST.append(sockfd)			# add the client socket to keep track of connected client
				print "Client connected"

			else:
				try:
					msg = msServer.receiveMessage(sock)	# receive the message sent from sock
					msgType = msg["message"]			# get the message
					
					if msgType == "auth":					# user first-time log into the server
						playerName = msg["params"]["name"]
						player = gameServer.newPlayer(playername, sock)
						gameServer.addPlayerOnline(player)

						obj = dict([("message", msgType), ("success", 1), ("player_id", player.getPlayerId())])
						print obj
						msServer.sendMessage(sock, obj)

					elif msgType == "refresh":				# get the list of the room in the server
						roomList = []
						for room in gameServer.getRoomList():
							roomTuple = [("id", room.getRoomId()), ("name", room.getRoomName())]
							roomList.append(roomTuple)

						obj = dict([("message", msgType), ("success", 1), ("room_list", roomList)])
						msServer.sendMessage(sock, obj)

					elif msgType == "create_room":			# player want to create a new room with the name
						roomName = msg["params"]["name"]
						room = gameServer.newRoom(roomName)
						gameServer.addRoom(room)

						obj = dict([("message", msgType), ("success", 1)])
						msServer.sendMessage(sock, obj)

					elif msgType == "join_room":			# player want to join the defined room
						roomId = msg["params"]["room_id"]
						roomTarget = gameServer.getRoomList()[roomId]

						# check if the room is full
						# if not full, add the player to the room
						if len(roomTarget.getPlayersInRoom()) < 5:
							roomTarget.addPlayerToRoom(msg["params"]["player_id"])
							obj = dict([("message", msgType), ("success", 1)])
						else:
							obj = dict([("message", msgType), ("success", 0)])
							
						msServer.sendMessage(sock, obj)

					elif msgType == "left_room":			# case if the player lefts the current room he was in
						roomId = msg["params"]["room_id"]
						roomTarget = gameServer.getRoomList()[roomId]

						roomTarget.deletePlayerFromRoom(msg["params"]["player_id"])
						if len(roomTarget.getPlayersInRoom()) == 0:
							# function to delete the room
							gameServer.deleteRoom(roomTarget)
							print "Room %d deleted! Room is empty" % (roomId)

						obj = dict([("message", msgType), ("success", 1)])
						msServer.sendMessage(sock, obj)

					

				except:
					if sock in CONNECTION_LIST:
						CONNECTION_LIST.remove(sock)
					broadcast_data(sock, "Client (%s, %s) is offline!" % addr)
					
					sock.close()
					
					continue

	servsock.close()
				