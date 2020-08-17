import numpy as np

#board default dimensions
HEIGHT = 10
WIDTH = 10

#direction constants
UP = (0,1)
DOWN = (0,-1)
RIGHT = (1,0)
LEFT = (-1,0)

class Game:
    def __init__(self, height = HEIGHT, width = WIDTH):
        self.height = height
        self.width = width
        #initialising a Snake object inside the constructor
        self.snake = Snake([(0,0), (1,0), (2,0), (3,0)], UP)

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

        head = self.snake.body[-1]
        body = self.snake.body[0:len(self.snake.body)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                #if i == head[0] and j == head[1]:
                #    print('X')
                #for k in range(len(body)):
                #    if i == body[0] and j== body[1] 
            





class Snake:
    #initialise the body and direction of snake in the beginning
    def __init__(self,init_position, init_direction):
        self.body = init_position
        self.direction = init_direction

    #position is a tuple
    #slices off the first tuple, and adds the new position. so snake can move forwards
    def take_step(self, position):
        self.body = self.body[1:] + position

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        #negative indexing means, last item in list
        return self.body[-1]



game = Game(10,10)
board1 = game.board_matrix()
game.render(board1)

