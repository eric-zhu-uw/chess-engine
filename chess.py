from bitarray import bitarray


A1, H1, A8, H8 = 91, 98, 21, 28

initial = (
    '         \n'  #   0 -  9
    '         \n'  #  10 - 19
    ' rnbqkbnr\n'  #  20 - 29
    ' pppppppp\n'  #  30 - 39
    ' ........\n'  #  40 - 49
    ' ........\n'  #  50 - 59
    ' ........\n'  #  60 - 69
    ' ........\n'  #  70 - 79
    ' PPPPPPPP\n'  #  80 - 89
    ' RNBQKBNR\n'  #  90 - 99
    '         \n'  # 100 -109
    '         \n'  # 110 -119
)

N, E, S, W = -10, 1, 10, -1
#curly braces are used to define a dictionary
directions = {
	'P': (N, N+N, N+W, N+E),
	'N': (N+N+W, N+N+E, E+E+N, E+E+S, S+S+E, S+S+W, W+W+S, W+W+N),
	'B': (N+E, S+E, S+W, N+W),					#
	'R': (N, E, S, W),							# multipless of these directions
	'Q': (N, N+E, E, S+E, S, S+W, W, N+W, N), 	#
	'K': (N, N+E, E, S+E, S, S+W, W, N+W, N)
}

class Position:

    def __init__(self, bitboard):
        self.bitboard = bitboard
        #find value of the board
        # wc
        # bc




def main():
    bitboard = {
        'P': bitarray('0000000011111111000000000000000000000000000000000000000000000000'),
        'N': bitarray('0100001000000000000000000000000000000000000000000000000000000000'),
        'B': bitarray('0010010000000000000000000000000000000000000000000000000000000000'),
        'R': bitarray('1000000100000000000000000000000000000000000000000000000000000000'),
        'Q': bitarray('0001000000000000000000000000000000000000000000000000000000000000'),
        'K': bitarray('0000100000000000000000000000000000000000000000000000000000000000'),
        'p': bitarray('0000000000000000000000000000000000000000000000001111111100000000'),
        'n': bitarray('0000000000000000000000000000000000000000000000000000000001000010'),
        'b': bitarray('0000000000000000000000000000000000000000000000000000000000100100'),
        'r': bitarray('0000000000000000000000000000000000000000000000000000000010000001'),
        'q': bitarray('0000000000000000000000000000000000000000000000000000000000010000'),
        'k': bitarray('0000000000000000000000000000000000000000000000000000000000001000'),

    }

    pos = Position(bitboard)
    print(pos.bitboard) #figure out how to encapsulate the bitboard
	

if __name__ == '__main__':
	main()