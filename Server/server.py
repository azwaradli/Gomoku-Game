import GameController
import MessageController

import socket, select

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

			else:
				try:
					msg = msServer.receiveMessage(sock)	# receive the message sent from sock
					msgType = msg["message"]			# get the message
					
					if msgType == "auth":
						playerName = msg["params"]["name"]
						player = gameServer.newPlayer(playername, sock)
						gameServer.addPlayerOnline(player)

						obj = dict([("message", msgType), ("success", 1)])
						msServer.sendMessage(sock, obj)

					elif msgType == "refresh":
						roomList = []
						for room in gameServer.getRoomList():
							roomTuple = [("id", room.getRoomId()), ("name", room.getRoomName())]
							roomList.append(roomTuple)

						obj = dict([("message", msgType), ("success", 1), ("room_list", roomList)])
						msServer.sendMessage(sock, obj)

					elif msgType == "create_room":
						roomName = msg["params"]["name"]
						room = gameServer.newRoom(roomName)
						gameServer.addRoom(room)

						obj = dict([("message", msgType), ("success", 1)])
						msServer.sendMessage(sock, obj)

					elif msgType == "join_room":
						roomId = msg["params"]["room_id"]
						roomTarget = gameServer.getRoomList()[roomId]

						if len(roomTarget.getPlayersInRoom()) < 5:
							roomTarget.addPlayerToRoom(msg["params"]["player_id"])
							obj = dict([("message", msgType), ("success", 1)])
						else:
							obj = dict([("message", msgType), ("success", 0)])
							
						msServer.sendMessage(sock, obj)

				except:
					if sock in CONNECTION_LIST:
						CONNECTION_LIST.remove(sock)
					broadcast_data(sock, "Client (%s, %s) is offline!" % addr)
					
					sock.close()
					
					continue

	servsock.close()
				