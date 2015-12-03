
LEGAL = 0

class Board(object):

	def __init__(self):
		# create 20x20 board
		super(Board, self).__init__()
		self.arrayBoard = [[LEGAL] * 20 for i in range(20)]

	def getBoard(self):
		return self.arrayBoard

	def placeBoard(self, x, y, pawn):
		if self.isLegal(x, y):
			self.arrayBoard[x][y] = pawn
			return True
		else:
			return False

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
		while temp >= 0 and self.arrayBoard[temp][y] == pawn and count < 5: # checking upper side
			temp -= 1
			count += 1

		temp = x + 1
		while temp < 20 and self.arrayBoard[temp][y] == pawn and count < 5: # checking lower side
			temp += 1
			count += 1

		if count >= 5:
			return True
		else:
			return False

	def horizontalChecking(self, x, y, pawn):
		count = 0
		temp = y - 1
		while temp > 0 and self.arrayBoard[x][temp] == pawn and count < 5: # checking left side
			temp -= 1
			count += 1

		temp = y + 1
		while temp < 20 and self.arrayBoard[x][temp] == pawn and count < 5: # checking right side
			temp += 1
			count += 1

		if count >= 5:
			return True
		else:
			return False

	def diagonalChecking(self, x, y, pawn):
		count = 0
		tempX = x + 1
		tempY = y - 1
		print "dig"
		while (tempX < 20 and tempY >= 0) and self.arrayBoard[tempX][tempY] == pawn and count < 5:
			# checking quadran 1
			tempX -= 1
			tempY -= 1
			count += 1

		tempX = x - 1
		tempY = y - 1
		while (tempX >= 0 and tempY >= 0) and self.arrayBoard[tempX][tempY] == pawn and count < 5:
			# checking quadran 2
			tempX -= 1
			tempY -= 1
			count += 1

		tempX = x - 1
		tempY = y + 1
		while (tempX >= 0 and tempY < 20) and self.arrayBoard[tempX][tempY] == pawn and count < 5:
			# checking quadran 3
			tempX -= 1
			tempY += 1
			count += 1

		tempX = x + 1
		tempY = y + 1
		while (tempX < 20 and tempY < 20) and self.arrayBoard[tempX][tempY] == pawn and count < 5:
			# checking quadran 4
			tempX += 1
			tempY += 1
			count += 1

		if count >= 5:
			return True
		else:
			return False


	def fiveRows(self, x, y, pawn):
		# is this placement form a 5 or more pawn in a line?
		
		if self.verticalChecking(x, y, pawn) or self.horizontalChecking(x, y, pawn) or self.diagonalChecking(x, y, pawn):
			return True
		else:
			return False


def main():
	board = Board()

	while 1:

		inp = raw_input('x y = ')
		data = inp.split()

		if board.placeBoard(int(data[0]), int(data[1]), 1):
			for row in board.getBoard():
				print row
			if board.fiveRows(int(data[0]), int(data[1]), 1):
				break
	
	print "you win"

if __name__ == '__main__':
	main()

