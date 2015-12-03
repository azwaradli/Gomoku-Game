class Room(object):

	def __init__(self, roomId, roomName):
		super(Room, self).__init__()
		self.roomId = roomId
		self.roomName = roomName
		self.playerList = []

	def getRoomId(self):
		return self.roomId

	def getRoomName(self):
		return self.roomName

	def getPlayersInRoom(self):
		return self.playerList

	def setRoomName(self, _name):
		self.roomName = _name

	def addPlayerToRoom(self, _player):
		self.playerList.append(_player)

	def deletePlayerFromRoom(self, _player):
		self.playerList.remove(_player)



# ROOM TESTING ONLY

def main():
	room = Room(1, "haha")
	print "%d %s" % (room.getRoomId(), room.getRoomName())
	print room.getPlayersInRoom()

	room.addPlayerToRoom("hello")
	room.addPlayerToRoom("sono")
	print room.getPlayersInRoom()

	room.deletePlayerFromRoom("sono")
	print room.getPlayersInRoom()

if __name__ == '__main__':
	main()
