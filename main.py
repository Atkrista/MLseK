import numpy as np

HEIGHT = 10
WIDTH = 10

class Game:
    def __init__(self, height = HEIGHT, width = WIDTH):
        self.height = height
        self.width = width

    def board_matrix(self):
        matrix = np.zeros(shape = (self.height, self.width), dtype = int)
        return matrix


    def render(self, board):
        #print the line on the top of the board
        for i in range(len(board)):
            print(" __", end ='')
        print()    
        #Print the actual board 
        for i in range(len(board)):
            print("|", end ='')
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    print('.  ', end ='')
                else:
                    print('#', end ='')
            print("|")

        #Print the line at the bottom of the board
        for i in range(len(board)):
            print(" --", end ='')
        print()

    


game = Game(10,10)
board1 = game.board_matrix()
game.render(board1)

