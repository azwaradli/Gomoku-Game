from Player import *
from Room import *

class GameController(object):
	
	def __init__(self):
		super(GameController, self).__init__()
		self.onlinePlayers = []
		self.roomList = []
		self.CURRENT_ONLINE_PLAYERS_ID = 1
		self.CURRENT_ROOMID = 1

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
		player = Player(self.CURRENT_ONLINE_PLAYERS_ID, name, sockfd)
		self.CURRENT_ONLINE_PLAYERS_ID += 1
		return player

	def newRoom(self, name):
		# create a new room
		room = Room(self.CURRENT_ROOMID, name)
		self.CURRENT_ROOMID += 1
		return room
		