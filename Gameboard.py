class Classicboard:
    '''The class representing the classic 3x3 TicTacToe board.
    '''
    Player1, Player2 = 'O', 'X'               #Not sure if this should be here or somewhere else

    def __init__(self):
        '''Initializes an empty game board.
        '''
        self.entries = {}
        for i in range(3):
            for j in range(3):
                self.entries[(i, j)] = '-'

    def __getitem__(self, pair):
        return self.entries[pair]

    def change(self, x, y, player):
        '''Checks if a spot is empty, and if so, changes it to the PLAYER icon.
        '''
        assert self[x,y] == '-', "Spot is already occupied!"
        self.entries[(x,y)] = player

    def str_row(self, row):
        return self[row, 0] + ' ' + self[row, 1] + ' ' + self[row, 2]

    def __str__(self):
        for i in range(2):
            print(self.str_row(i))
        return self.str_row(2)

class Bigboard(Classicboard):
    def __init__(self):
        self.position = None
        Classicboard.__init__(self)
        for key, value in self.entries.items():
            self.entries[key] = Classicboard()

    def change(self, x, y, player):
        '''Changes the icon of a chosen spot in the board found at self.position
        (subject to the constraints of the change method in Classicboard) and
        updates self.position.
        '''
        self[self.position].change(x, y, player)
        self.position = (x, y)

    def str_row(self, b_row, row):
        '''Prints a row across three boards.
        '''
        rstring = ''
        for i in range(3):
            rstring += self[b_row, i].str_row(row) + '   '
        return rstring.strip()

    def __str__(self):
        for i in range(3):
            for j in range(3):
                print(self.str_row(i, j))
            print('\n')
        return "Current board (zero-indexed): " + str(self.position)
