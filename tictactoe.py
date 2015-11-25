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
    ''' Board class, takes in a player1 object and player2 object
        Creates an empty board like:
            None None None --> A1 A2 A3
            None None None --> B1 B2 B3
            None None None --> C1 C2 C3
    '''
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.A1, self.A2, self.A3 = [None]*3
        self.B1, self.B2, self.B3 = [None]*3
        self.C1, self.C2, self.C3 = [None]*3
        self.board = [self.A1, self.A2, self.A3,
                      self.B1, self.B2, self.B3,
                      self.C1, self.C2, self.C3]

    def _printer(self):
        return "{a1}\t{a2}\t{a3}\n"\
                "{b1}\t{b2}\t{b3}\n"\
                "{c1}\t{c2}\t{c3}\n".format(a1=self.A1, a2=self.A2, a3=self.A3,
                                            b1=self.A1, b2=self.A2, b3=self.A3,
                                            c1=self.A1, c2=self.A2, c3=self.A3
                                            )

    def __str__(self):
        return self._printer()

    def __repr__(self):
        return self._printer()


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


def play():
    ''' backgound: create board.
                   create players
        ask player1 for x or o
            assign player 2 the remaining of [x/o]
        until (victory of p1/p2) or draw (no place in board is None and no victory ):
            keep asking for turns from p1, p2 alternatively
    '''

    mlist = ['x', 'o']
    n1, m1 = str(raw_input('Player 1, enter name and marker: ')).split()
    n2 = str(raw_input('Player 2, enter name: '))
    if m1 == mlist[0]:
        m2 = mlist[1]
    else:
        m2 = mlist[0]
    print '{p} your marker is set to {m}'.format(p=n2, m=m2)

    p1 = Player(n1, m1)
    p2 = Player(n2, m2)

    board = Board(p1, p2)
    print board


if __name__ == '__main__':
    play()
