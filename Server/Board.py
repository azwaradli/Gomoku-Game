class Board(object):
	def __init__(self):
		# create 20x20 board
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

	def verticalChecking(x, y):
		if x - 4 < 0:	# upper boundary
			iteration = x + 1	# get iteration based on left value on boundary
			
		elif x + 4 > 20:	# lower boundary
			iteration = 20 - x
			
		else:	# don't have boundary
			iteration = 4

		while iteration > 0 and result == False:
			temp = x 	# moving x variable
			count = 0				
			for i in range (4, 1): # check if x+4 to x contains pawn
				if self_board[temp+i][y] != pawn:
					break
				else:
					count++
			if count == 5:
				return True
			temp--
			iteration--

		return False

	def horizontalChecking(x, y):
		if y - 4 < 0:	# upper boundary
			iteration = y + 1	# get iteration based on left value on boundary
			
		elif y + 4 > 20:	# lower boundary
			iteration = 20 - y
			
		else:	# don't have boundary
			iteration = 4

		while iteration > 0 and result == False:
			temp = y 	# moving x variable
			count = 0				
			for i in range (4, 1): # check if x+4 to x contains pawn
				if self_board[x][temp+i] != pawn:
					break
				else:
					count++
			if count == 5:
				return True
			temp--
			iteration--

		return False

	def diagonalChecking(x, y):

	def fiveRows(self, x, y):
		# is this placement form a 5 or more pawn in a line?
		
		if verticalChecking(x, y) == True:
			return True
		elif horizontalChecking(x, y) == True:
			return True
		# elif diagonalChecking(x, y):
		# 	return True
		else
			return False
