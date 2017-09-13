from evaluate import evaluate
from moves import moves
from itertools import count	# https://docs.python.org/2/library/itertools.html#itertools.count
#UNDERSTANDING YIELD http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

# Two basic algorithms to apply are:
#		1. minmax
#												[starting position 1.5]													START
#				[p1 2.5]    						   [p2 0]      					 	[p3 1.5]					MAX
#	[p1.1 0] [p1.2 3.5] [p1.3 2.5] # [p2.1 -1] [p2.2 0] [p2.3 3] # [p3.1 0] [p3.2 1.5] [p3.3 5]	MIN


#		2. alpha-beta pruning
#				Essentially sets the lower||upper bound stating,
#				"no one would put themselves in a worse after the move compared to before"

#		3. quicessence search "quiet position"


# Head
#   key
#   value
#   listofPositions

# class Position should store:
#		1. board 		--> position of all of the current pieces [10x10]
#		2. value				--> score of the position
#		3. validPositions	--> following Posititions

DEPTH = 4

class Position:

	def __init__(self, board, wc, bc, depth):	#white castle, black castle
		self.board = board
		self.wc = wc
		self.bc = bc
		self.depth = depth
		self.listOfPos = []
		self.value = 'x'
		if depth == DEPTH:
			self.value = evaluate(board)
		if depth < DEPTH:
			self.moves = moves(board)
			for x in self.moves:
				self.listOfPos.append(rotate(x, wc, bc, depth))

		# turn the array into boards for the opposite side

def printBoard(board):
	print('//==============================//')
	for i, x in enumerate(board):
		if(i != 0 and i % 10 == 0):
			print('          ')
		print(x, end = " ")
	print()
	print('//==============================//')

def printPosTree(pos):
	printBoard(pos.board)
	print(pos.value)
	if(pos.depth < DEPTH):
		for x in pos.listOfPos:
			printPosTree(x)

def rotate(board, wc, bc, depth):
	return Position(board[::-1].swapcase(), wc, bc, depth+1)
	# since you are always switching sides... you always want to maximize score

def findMax(listOfPos):
	curMax = -100000
	for x in listOfPos:
		if x.value == 'x':
			x.value = findMax(x.listOfPos)
		curMax = max(curMax, x.value)
	return curMax

def minimax(pos):
	return findMax(pos.listOfPos)

def oneDepthMax(listOfPos):
	curMax = -100000
	curPos = listOfPos[0]			#questionable assignment
	for x in listOfPos:
		if x.value > curMax:
			curMax = x.value
			curPos = x
	return curPos



if __name__ == '__main__':
	board = (				#type of string
		'..........'
		'.rnbqkbnr.'
		'.pppppppp.'
		'.        .'
		'.        .'
		'.        .'
		'.        .'
		'.PPPPPPPP.'
		'.RNBQKBNR.'
		'..........'
	)

	board2 = (
		'..........'
		'.r b k nr.'
		'.pp pppbp.'
		'.  n   p .'
		'.        .'
		'.    PP  .'
		'.  P     .'
		'.PP N  PP.'
		'.R  Q RK .'
		'..........'
	)



	pos = Position(board2, 3, 3, 0)
	printBoard(board2)
	minimax(pos)	
	nextPos = oneDepthMax(pos.listOfPos)
	printBoard(nextPos.board)

