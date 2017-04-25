from itertools import count	# https://docs.python.org/2/library/itertools.html#itertools.count

A1, H1, A8, H8 = 81, 88, 21, 28
N, E, S, W = -10, 1, 10, -1
#curly braces are used to define a dictionary
directions = {
	'P': (N, N+N, N+W, N+E),
	'N': (N+N+W, N+N+E, E+E+N, E+E+S, S+S+E, S+S+W, W+W+S, W+W+N),
	'B': (N+E, S+E, S+W, N+W),					#
	'R': (N, E, S, W),							# multipless of these directions
	'Q': (N, N+E, E, S+E, S, S+W, W, N+W), 	#
	'K': (N, N+E, E, S+E, S, S+W, W, N+W)
}

# STILL NEED TO DEAL WITH CASTLING & if move is legal
def moves(board):
	for i, p in enumerate(board):

			if not p.isupper(): continue
			for d in directions[p]:
				for j in count(i+d, d):	# keep going by multiple of direction DOCUMENTATION
					# print("p: ", p, "| d: ", d, " | ", i, " ", j) # IMPORTANT FOR TESTING
					if j > 99 or j < 0: break
					q = board[j]
					if q == '.' or q.isupper(): break

					if p == 'P':
						if d in (N, N+N) and q != ' ': break
						if d == N+N and (i < A1+N or board[i+N] != ' '): break	#check if on 2nd rank & first space is empty
						if d in (N+W, N+E) and q == ' ': break 		# and j not in (self.ep, self.kp)
						newBoard = list(board)
						newBoard[j] = newBoard[i]
						newBoard[i] = ' '
						newBoard = ''.join(newBoard)
						yield newBoard		#http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
						break
					elif p == 'N':
						newBoard = list(board)
						newBoard[j] = newBoard[i]
						newBoard[i] = ' '
						newBoard = ''.join(newBoard)
						yield newBoard
						break
					elif p == 'B':
						newBoard = list(board)
						temp = newBoard[j]
						newBoard[j] = newBoard[i]
						newBoard[i] = ' '
						newBoard = ''.join(newBoard)
						yield newBoard
						if temp.islower():
							break
					elif p == 'R':
						newBoard = list(board)
						temp = newBoard[j]
						newBoard[j] = newBoard[i]
						newBoard[i] = ' '
						newBoard = ''.join(newBoard)
						yield newBoard
						if temp.islower():
							break
					elif p == 'Q':
						newBoard = list(board)
						temp = newBoard[j]
						newBoard[j] = newBoard[i]
						newBoard[i] = ' '
						newBoard = ''.join(newBoard)
						yield newBoard
						if temp.islower():
							break
					elif p == 'K':
						newBoard = list(board)
						newBoard[j] = newBoard[i]
						newBoard[i] = ' '
						newBoard = ''.join(newBoard)
						yield newBoard
						break
