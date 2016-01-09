class Classicboard:
    '''The class representing the classic 3x3 TicTacToe board.
    '''
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

    def disp_row(self, row):
        return self[0, row] + self[1, row] + self[2, row]

    def __str__(self):
        for i in range(2):
            print(self.disp_row(i))
        return self.disp_row(2)

class Bigboard(Classicboard):
    def __init__(self):
        Classicboard.__init__(self)
        for key, value in self.entries.items():
            self.entries[key] = Classicboard()
