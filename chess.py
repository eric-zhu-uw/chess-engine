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

class Position(namedtuple('Position', 'board score wc bc ep kp')):



def main():
	print(initial)

if __name__ == '__main__':
	main()