
# evaluate(board) is given a 10x10 board and evaluates the chessboard position
# f(p) = 200(K-K')
		# + 9(Q-Q')
		# + 5(R-R')
		# + 3(B-B' + N-N')
		# + 1(P-P')
		# - 0.5(D-D' + S-S' + I-I')
		# + 0.1(M-M') + ...
		# KQRBNP = number of kings, queens, rooks, bishops, knights and pawns
		# D,S,I = doubled, blocked and isolated pawns
		# M = Mobility (the number of legal moves)
# params: listof(listof Char)
# return: int

# more accurate evaluation function to care about board position !!!
def evaluate(board):
		score = 0

		for i, x in enumerate(board):
				if x == '.':
					continue
				elif x == 'P':
						score += 1
						if board[i - 10] == 'P':
							score -= 0.5
				elif x == 'p':
					score -= 1
					if board[i + 10] == 'p':
						score -= 0.5
				elif x == 'K':
					score += 200
				elif x == 'k':
					score -= 200
				elif x == 'Q':
					score += 9
				elif x == 'q':
					score -= 9
				elif x == 'R':
					score += 5
				elif x == 'r':
					score -= 5
				elif x == 'B':
					score += 3
				elif x == 'b':
					score -= 3
				elif x == 'N':
					score += 3
				elif x == 'n':
					score -= 3
				else:
					continue
					#square was empty
		return score