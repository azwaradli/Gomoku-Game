from Board import *

class Game(object):
	
	def __init__(self, r_id):
		super(Game, self).__init__()
		self.roomId = r_id
		self.board = Board()			# board for a game
		self.playerList = []			# player enlisted in game
		self.turn = 0					# player turn
		self.isStarted = False
		self.gameWinner = -1

	def isGameStarted(self):
		return self.isStarted

	def startGame(self):
		# pre-condition: player signed to the game are more than 3
		self.isStarted = True

	def endGame(self):
		self.isStarted = False

	def getWinner(self):
		return self.gameWinner

	def setWinner(self, _player):
		self.gameWinner = _player

	def getPlayerList(self):
		return self.playerList

	def addPlayerToGame(self, _player):
		self.playerList.append(_player)

	def deletePlayerFromGame(self, _player):
		self.playerList.remove(_player)

	def placePlayerPawn(self, x, y, _player):
		if self.board.isCellEmpty(x, y):
			self.board.placeBoard(x, y, _player.getPawn())
			if self.board.fiveRows(x, y, _player.getPawn()):
				self.endGame()
				self.setWinner(_player.getPlayerId())
			else:
				turn = (turn + 1) % len(playerList)
			return True
		else:
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