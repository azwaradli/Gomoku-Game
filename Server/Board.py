class Board(object):
	def __init__(self):
		super(Board, self).__init__()
		self.array_board = [[0] * 20 for i in range(20)]

	def placeBoard(self, x, y, pawn):
		self.array_board[x][y] = pawn

	def isCellEmpty(self, x, y):
		return self.array_board[x][y] == 0

	def isCellPlayer(self, x, y, pawn):
		return self.array_board[x][y] == pawn

	def checkBoard(self, player):
		# check if a player is winning
		# by placing its pawn 5 in a row
		# STUB: still waiting for Game Logics
		return True