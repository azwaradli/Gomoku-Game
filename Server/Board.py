class Board(object):

	LEGAL = 0

	def __init__(self):
		# create 20x20 board
		super(Board, self).__init__()
		self.arrayBoard = [[LEGAL] * 20 for i in range(20)]

	def getBoard(self):
		return self.array_board

	def placeBoard(self, x, y, pawn):
		if isLegal(self, x, y):
			self.arrayBoard[x][y] = pawn

	def isLegal(self, x, y):
		return self.arrayBoard[x][y] == LEGAL

	def checkBoard(self, player):
		# check if a player is winning
		# by placing its pawn 5 in a row
		# STUB: still waiting for Game Logics
		return True

	def verticalChecking(self, x, y, pawn):
		count = 0
		temp = x - 1
		while temp > 0 and selfBoard[temp][y] != pawn and count < 5: # checking upper side
			temp--
			count++

		temp = x + 1
		while temp < 20 and selfBoard[temp][y] != pawn and count < 5: # checking lower side
			temp++
			count++

		if count >= 5
			return True
		else
			return False

	def horizontalChecking(self, x, y, pawn):
		count = 0
		temp = y - 1

		while temp > 0 and selfBoard[x][temp] != pawn and count < 5: # checking left side
			temp--
			count++

		temp = y + 1
		while temp < 20 and selfBoard[x][temp] != pawn and count < 5: # checking right side
			temp++
			count++

		if count >= 5
			return True
		else
			return False

	def diagonalChecking(self, x, y, pawn):
		count = 0
		tempX = x + 1
		tempY = y - 1
		while (tempX < 20 and tempY >= 0) and selfBoard[tempX][tempY] != pawn and count < 5:
			# checking quadran 1
			tempX--
			tempY--
			count++

		tempX = x - 1
		tempY = y - 1
		while (tempX >= 0 and tempY >= 0) and selfBoard[tempX][tempY] != pawn and count < 5:
			# checking quadran 2
			tempX--
			tempY--
			count++

		tempX = x - 1
		tempY = y + 1
		while (tempX >= 0 and tempY < 20) and selfBoard[tempX][tempY] != pawn and count < 5:
			# checking quadran 3
			tempX--
			tempY++
			count++

		tempX = x + 1
		tempY = y + 1
		while (tempX < 20 and tempY < 20) and selfBoard[tempX][tempY] != pawn and count < 5:
			# checking quadran 4
			tempX++
			tempY++
			count++

		if count >= 5:
			return True
		else:
			return False


	def fiveRows(self, x, y, pawn):
		# is this placement form a 5 or more pawn in a line?
		
		if verticalChecking(self, x, y, pawn) or
			horizontalChecking(self, x, y, pawn) or 
			diagonalChecking(self, x, y, pawn):
			return True
		else
			return False
