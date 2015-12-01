class Room(object):

	def __init__(self, r_id, r_name):
		super(Room, self).__init__()
		self.room_id = r_id
		self.room_name = r_name
		self.player_list = []

	def getRoomId(self):
		return self.room_id

	def getRoomName(self):
		return self.room_name

	def getPlayersInRoom(self):
		return self.player_list

	def setRoomName(self, _name):
		self.room_name = _name

	def addPlayerToRoom(self, _player):
		self.player_list.append(_player)

	def deletePlayerFromRoom(self, _player):
		self.player_list.remove(_player)



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
