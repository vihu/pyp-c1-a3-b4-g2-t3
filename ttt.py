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
        self._inputs = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        self.board = {i: ' ' for i in self._inputs}

    def _printer(self):
        b = self.board
        return ("\n_{}_|_{}_|_{}_".format(b['A1'], b['A2'], b['A3']) + '\n'
                "_{}_|_{}_|_{}_".format(b['B1'], b['B2'], b['B3']) + '\n'
                "_{}_|_{}_|_{}_\n".format(b['C1'], b['C2'], b['C3'])
                )

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
            if self.board[move] is ' ':
                self.board[move] = player.marker
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

    print '\n Let the game begin... \n'

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


def check_victory(player, board):
    ''' Iterating through a list of winning combinations, perform a
    check to see that all values are equal. Returns True or False '''

    victory_combos = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'],
                      ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'],
                      ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['A1', 'B2', 'C3']]

    for combo in victory_combos:
        check = all(board[e] == player.marker for e in combo)
        if check:
            print "Player {n} has won!.".format(n=player.name)
            print board
            return True
    return False


def play():
    ''' until (victory of p1/p2) or draw (no place in board is ' ' and no victory)
        keep asking for turns from p1, p2 alternatively
    '''
    b = initialize_game()

    for turn in whose_turn():
        print b

        if turn == 1:
            # player one makes a move
            p1move = raw_input('{p1} make your move: '.format(p1=b.p1.name))
            while isinstance(b.update(b.p1, p1move), MoveError):
                p1move = raw_input('{p1} make your move: '.
                                   format(p1=b.p1.name))
            if check_victory(b.p1, b.board):
                break

        else:
            # player two makes a move
            p2move = raw_input('{p2} make your move: '.format(p2=b.p2.name))
            while isinstance(b.update(b.p2, p2move), MoveError):
                p2move = raw_input('{p2} make your move: '.
                                   format(p2=b.p2.name))
            if check_victory(b.p2, b.board):
                break

    print b
    print "Game Over."
    return


if __name__ == '__main__':
    play()
