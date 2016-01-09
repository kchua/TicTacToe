class Classicboard:
    '''The class representing the classic 3x3 TicTacToe board.
    '''
    def __init__(self):
        self.entries = {}
        for i in range(3):
            for j in range(3):
                self.entries[(i, j)] = '-'

class Bigboard(Classicboard):
    def __init__(self):
        Classicboard.__init__(self)
        for key, value in self.entries.items():
            self.entries[key] = Classicboard()
