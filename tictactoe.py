'''
Write a simple program to play a game of Tic-Tac-Toe. The game is between two
players. The computer starts displaying the board with all the empty spots and
asks for the first move. The computer asks each player for her move; the player
will inform the coordinates to place her mark with a letter and a number; the
letter indicating the column and the number the row. Example: B2 is the center
of the board. A1 is the top left corner of the board. C3 is the bottom
right corner (furthermost from the A1).

The computer will keep asking both player for their marks until one of them win
or there are no more places in the board to position marks.
'''
import weakref


class Board(object):
    def __init__(self):
        self.board = [[None]*3]*3
        self._a = self.board[0]
        self._b = self.board[1]
        self._c = self.board[2]


class MarkerError(Exception):
    pass


class MarkerDescriptor(object):
    def __init__(self):
        self.data = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data[instance]

    def __set__(self, instance, value):
        if value not in ['X', 'x', 'o', 'O']:
            raise MarkerError('Only Xs and Os are allowed in tic tac toe')
        else:
            self.data[instance] = value


class Mark(object):
    # use X or O as markers
    marker = MarkerDescriptor()

    def __init__(self, marker):
        self.marker = marker

    def __repr__(self):
        return 'Mark({})'.format(self.marker)


class Player(object):
    def __init__(self, choice):
        self.choice = Mark(choice)

    def __repr__(self):
        return 'Player({})'.format(self.choice)
