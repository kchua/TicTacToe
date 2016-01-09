class Classicboard:
    '''The class representing the classic 3x3 TicTacToe board.
    '''

    def __init__(self):
        '''Initializes an empty game board.
        '''
        self.entries = {}
        self.winner = None
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
        if self.diagonal(player) or self.row(player) or self.column(player):
            self.winner = player
            for i in range(3):
                for j in range(3):
                    self.entries[(i, j)] = self.winner

    def str_row(self, row):
        return self[0, row] + ' ' + self[1, row] + ' ' + self[2, row]

    def __str__(self):
        for i in range(2):
            print(self.str_row(i))
        return self.str_row(2)

    def diagonal(self, player):
        return ((checker(self[0,0], self[1,1], self[2,2]) and self[0,0] == player) or
                (checker(self[2,0], self[1,1], self[0,2]) and self[2,0] == player))

    def column(self, player):
        return any([checker(self[i,0], self[i,1], self[i,2]) and self[i,0] == player
            for i in range(3)])

    def row(self, player):
        return any([checker(self[0,i], self[1,i], self[2,i]) and self[0,i] == player
            for i in range(3)])

class Bigboard(Classicboard):
    def __init__(self):
        self.position = None
        Classicboard.__init__(self)
        for key, _ in self.entries.items():
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
            rstring += self[i, b_row].str_row(row) + '   '
        return rstring.strip()

    def __str__(self):
        for i in range(3):
            for j in range(3):
                print(self.str_row(i, j))
            print('\n')
        return "Current board (zero-indexed): " + str(self.position)

############################### Functions ######################################

def checker(s1, s2, s3):
    return s1 == s2 and s2 == s3
