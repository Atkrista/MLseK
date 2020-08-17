import numpy as np

#board default dimensions
HEIGHT = 10
WIDTH = 10

#direction constants
UP = (0,1)
DOWN = (0,-1)
RIGHT = (1,0)
LEFT = (-1,0)

#Initial positions of Snake
INITIAL = [(0,0), (1,0), (2,0), (3,0)]
HEAD = INITIAL[-1]
BODY = INITIAL[1:]

class Game:
    def __init__(self, height = HEIGHT, width = WIDTH):
        self.height = height
        self.width = width
        #initialising a Snake object inside the constructor
        self.snake = Snake(INITIAL, UP)

    def board_matrix(self):
        matrix = np.zeros(shape = (self.height, self.width), dtype = int)
        return matrix

    def char_to_print(board, i, j):
        if (i,j) == (HEAD[0],HEAD[1]):
            return 'X'
        elif (i,j) in BODY: 
            return 'O'
        else:
            return ' '
        

    def render(self, board):
        #print the line on the top of the board
        print("+" + self.width * '--' + "+" )
        for i in range(len(board)):
            print("|", end ='')
            for j in range(len(board[0])):
                print(self.char_to_print(self.height -1- i, self.width-1- j) + ' ' , end ='')
            print("|")

        #Print the line at the bottom of the board
        print("+" + self.width * '--' + "+" )
        
        print()

        head = self.snake.body[-1]
        body = self.snake.body[0:len(self.snake.body)]



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

