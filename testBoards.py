from evaluate import evaluate
from moves import moves
from schematics import Position, printBoard, moves

boardTestKnight = (
		'..........'
		'.rnbqkbnr.'
		'.pppppppp.'
		'.  N  N  .'
		'.        .'
		'.        .'
		'.        .'
		'.PPPPPPPP.'
		'.R BQKB R.'
		'..........'
	)

boardTestBishop = (
		'..........'
		'.rnbqkbnr.'
		'.pppppppp.'
		'.        .'
		'.   BB   .'
		'.   PP   .'
		'.        .'
		'.PPP  PPP.'
		'.RN QK NR.'
		'..........'
	)

boardTestRook = (
		'..........'
		'.rnbqkbnr.'
		'.pppppppp.'
		'.        .'
		'.   RR   .'
		'.P      P.'
		'.        .'
		'. PPPPPP .'
		'. NBQKBN .'
		'..........'
	)

boardTestQueen = (
		'..........'
		'.rnbqkbnr.'
		'.pppppppp.'
		'.        .'
		'.    Q   .'
		'.   P    .'
		'.        .'
		'.PPP PPPP.'
		'.RNB KBNR.'
		'..........'
	)

boardTestKing = (
		'..........'
		'.rnbqkbnr.'
		'.pppppppp.'
		'.        .'
		'.   K    .'
		'.    P   .'
		'.        .'
		'.PPPP PPP.'
		'.RNBQ BNR.'
		'..........'
	)

boardTestPawn = (
		'..........'
		'.rnbqkbnr.'
		'.pppp ppp.'
		'.P       .'
		'.   pp   .'
		'. P  PP  .'
		'. P      .'
		'.   P  PP.'
		'.RNBQKBNR.'
		'..........'
	)

def testBoard(board):
	posMoves = Position(board)
	printBoard(board)
	print(posMoves.value)
	print(posMoves.moves)
	for x in posMoves.moves:
		printBoard(x)

# to test if all possible moves are generated --> insert board in testBoard()
# STILL NEED TO DEAL WITH CASTLING & if move is legal
if __name__ == '__main__':
	testBoard(boardTestPawn)