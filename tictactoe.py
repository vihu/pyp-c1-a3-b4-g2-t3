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
from itertools import cycle


class Board(object):
    ''' Board class, takes in a player1 object and player2 object
        Creates an empty board like:
            None None None --> A1 A2 A3
            None None None --> B1 B2 B3
            None None None --> C1 C2 C3
        board is a single dimension list:
        ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        where everything is set to None at the start
    '''
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.board = [None]*9
        self._inputs = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

    def _printer(self):
        return self.board

    def __str__(self):
        return str(self._printer())

    def __repr__(self):
        return self._printer()

    def update(self, player, move):
        if move not in self._inputs:
            print MoveError('Correct set of inputs are: {}'.
                            format(self._inputs))
            return MoveError('Correct set of inputs are: {}'.
                             format(self._inputs))
        else:
            if move == 'A1' and self.board[0] is None:
                self.board[0] = player.marker
                print self.board
            elif move == 'A2' and self.board[1] is None:
                self.board[1] = player.marker
                print self.board
            elif move == 'A3' and self.board[2] is None:
                self.board[2] = player.marker
                print self.board
            elif move == 'B1' and self.board[3] is None:
                self.board[3] = player.marker
                print self.board
            elif move == 'B2' and self.board[4] is None:
                self.board[4] = player.marker
                print self.board
            elif move == 'B3' and self.board[5] is None:
                self.board[5] = player.marker
                print self.board
            elif move == 'C1' and self.board[6] is None:
                self.board[6] = player.marker
                print self.board
            elif move == 'C2' and self.board[7] is None:
                self.board[7] = player.marker
                print self.board
            elif move == 'C3' and self.board[8] is None:
                self.board[8] = player.marker
                print self.board
            else:
                print MoveError('Input already occupied')
                return MoveError('Input already occupied')


class MoveError(Exception):
    pass


class PlayerError(Exception):
    pass


class MarkerError(Exception):
    pass


class TypeConstraint(object):
    def __init__(self, constraint):
        self.constraint = constraint
        self.data = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data[instance]

    def __set__(self, instance, value):
        if not isinstance(value, self.constraint):
            raise PlayerError('Not a valid name')
        else:
            self.data[instance] = value


class MarkerConstraint(TypeConstraint):
    def __set__(self, instance, value):
        if value not in ['X', 'x', 'O', 'o']:
            raise MarkerError('Only x and o allowed for markers.')
        else:
            self.data[instance] = value


class Player(object):
    ''' Player class, take in a name(str), and a marker(x/o)
    '''
    name = TypeConstraint(str)
    marker = MarkerConstraint(str)

    def __init__(self, name, marker):
        self.marker = marker
        self.name = name

    def __repr__(self):
        return 'Player({n},{m})'.format(n=self.name, m=self.marker)


def initialize_game():
    ''' backgound: create board.
                   create players
        ask player1 for x or o
            assign player 2 the remaining of [x/o]
        returns the playing board with players with their markers added
            to the board object
    '''
    n1 = raw_input('Player 1, enter name: ')
    m1 = raw_input('{p1} choose your marker (x/o/X/O): '.format(p1=n1))
    n2 = raw_input('Player 2, enter name: ')

    if m1 == 'X':
        m2 = 'O'
    elif m1 == 'x':
        m2 = 'o'
    elif m1 == 'o':
        m2 = 'x'
    else:
        m2 = 'X'

    print '{p} your marker is set to {m}'.format(p=n1, m=m1)
    print '{p} your marker is set to {m}'.format(p=n2, m=m2)
    print
    print 'Let the game begin...'
    print

    p1 = Player(n1, m1)
    p2 = Player(n2, m2)

    board = Board(p1, p2)
    return board


def whose_turn():
    max_moves = 8
    move = 0
    for turn in cycle(range(1, 3)):
        if move < max_moves:
            move += 1
            yield turn
        else:
            break


def play():
    ''' until (victory of p1/p2) or draw (no place in board is None and no victory)
        keep asking for turns from p1, p2 alternatively
    '''
    b = initialize_game()
    print b

    for turn in whose_turn():
        if turn == 1:
            # player one makes a move
            p1move = raw_input('{p1} make your move: '.format(p1=b.p1.name))
            while isinstance(b.update(b.p1, p1move), MoveError):
                p1move = raw_input('{p1} make your move: '.
                                   format(p1=b.p1.name))
        else:
            # player two makes a move
            p2move = raw_input('{p2} make your move: '.format(p2=b.p2.name))
            while isinstance(b.update(b.p2, p2move), MoveError):
                p2move = raw_input('{p2} make your move: '.
                                   format(p2=b.p2.name))


if __name__ == '__main__':
    play()
