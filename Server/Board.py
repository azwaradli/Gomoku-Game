
LEGAL = 0

class Board(object):

	def __init__(self):
		# create 20x20 board
		super(Board, self).__init__()
		self.arrayBoard = [[LEGAL] * 20 for i in range(20)]

	def getBoard(self):
		return self.arrayBoard

	def placeBoard(self, row, col, pawn):
		if self.isLegal(row, col):
			self.arrayBoard[row][col] = pawn
			return True
		else:
			return False

	def isLegal(self, row, col):
		return self.arrayBoard[row][col] == LEGAL

	def checkBoard(self, player):
		# check if a player is winning
		# bcol placing its pawn 5 in a row
		# STUB: still waiting for Game Logics
		return True

	def verticalChecking(self, row, col, pawn):
		count = 0
		temp = row - 1
		while temp >= 0 and self.arrayBoard[temp][col] == pawn and count < 4: # checking upper side
			temp -= 1
			count += 1

		temp = row + 1
		while temp < 20 and self.arrayBoard[temp][col] == pawn and count < 4: # checking lower side
			temp += 1
			count += 1

		if count >= 4:
			return True
		else:
			return False

	def horizontalChecking(self, row, col, pawn):
		count = 0
		temp = col - 1
		while temp > 0 and self.arrayBoard[row][temp] == pawn and count < 4: # checking left side
			print str(temp) + " upper"
			temp -= 1
			count += 1

		temp = col + 1
		while temp < 20 and self.arrayBoard[row][temp] == pawn and count < 4: # checking right side
			print str(temp) + " lower"
			temp += 1
			count += 1

		if count >= 4:
			return True
		else:
			return False

	def diagonalChecking(self, row, col, pawn):
		count = 0
		tempRow = row + 1
		tempCol = col - 1
		print "dig"
		while (tempRow < 20 and tempCol >= 0) and self.arrayBoard[tempRow][tempCol] == pawn and count < 4:
			# checking quadran 1
			tempRow -= 1
			tempCol -= 1
			count += 1

		tempRow = row - 1
		tempCol = col - 1
		while (tempRow >= 0 and tempCol >= 0) and self.arrayBoard[tempRow][tempCol] == pawn and count < 4:
			# checking quadran 2
			tempRow -= 1
			tempCol -= 1
			count += 1

		tempRow = row - 1
		tempCol = col + 1
		while (tempRow >= 0 and tempCol < 20) and self.arrayBoard[tempRow][tempCol] == pawn and count < 4:
			# checking quadran 3
			tempRow -= 1
			tempCol += 1
			count += 1

		tempRow = row + 1
		tempCol = col + 1
		while (tempRow < 20 and tempCol < 20) and self.arrayBoard[tempRow][tempCol] == pawn and count < 4:
			# checking quadran 4
			tempRow += 1
			tempCol += 1
			count += 1

		if count >= 4:
			return True
		else:
			return False


	def fiveRows(self, row, col, pawn):
		# is this placement form a 5 or more pawn in a line?
		
		if self.verticalChecking(row, col, pawn) or self.horizontalChecking(row, col, pawn) or self.diagonalChecking(row, col, pawn):
			return True
		else:
			return False


def main():
	board = Board()

	while 1:

		inp = raw_input('row col = ')
		data = inp.split()

		if board.placeBoard(int(data[0]), int(data[1]), 1):
			for row in board.getBoard():
				print row
			if board.fiveRows(int(data[0]), int(data[1]), 1):
				break
	
	print "win"

if __name__ == '__main__':
	main()

