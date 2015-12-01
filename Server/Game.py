class Game(object):
	
	def __init__(self, r_id):
		super(Game, self).__init__()
		self.room_id = r_id
		self.board = Board()			# board for a game
		self.player_list = []			# player enlisted in game
		self.turn = 0					# player turn

	def getPlayerList(self):
		return self.player_list

	def addPlayerToGame(self, _player):
		self.player_list.append(_player)

	def deletePlayerFromGame(self, _player):
		self.player_list.remove(_player)

	def placePlayerPawn(self, x, y, _player):
		if self.board.isCellEmpty(x, y):
			self.board.placeBoard(x, y, _player.getPawn())
			turn = (turn + 1) % len(player_list)
			return True
		else
			return False

	def getTurn(self):
		return self.turn
		

# GAME TESTING ONLY

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

		