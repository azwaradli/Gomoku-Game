import MessageController

class GameController(object):

	MAX_PLAYERS_PER_ROOM = 5
	MAX_ROOM_ALLOWED = 3
	CURRENT_ROOMID = 1
	CURRENT_ONLINE_PLAYERS_ID = 1
	
	def __init__(self):
		super(GameController, self).__init__()
		self.onlinePlayers = []
		self.roomList = []

	def getRoomList(self):
		# get available room list
		return self.roomList

	def getOnlinePlayers(self):
		# get players online
		return self.onlinePlayers

	def addPlayerOnline(self, newplayer):
		# precondition = player is less than 5
		self.onlinePlayers.append(newplayer)

	def deletePlayerOnline(self, player):
		# precondition = players online not zero and _player exists
		self.onlinePlayers.remove(player)

	def addRoom(self, room):
		# precondition = total rooms are less than 3
		self.roomList.append(room)

	def deleteRoom(self, room):
		# precondition = total rooms not zero and room exists
		self.roomList.remove(room)

	def newPlayer(self, name, sockfd):
		# creating a new player
		player = Player(CURRENT_ONLINE_PLAYERS_ID, sockfd, name)
		CURRENT_ONLINE_PLAYERS_ID += 1
		return player

	def newRoom(self, name):
		# create a new room
		room = Room(CURRENT_ROOMID, name)
		CURRENT_ROOMID += 1
		return room
		