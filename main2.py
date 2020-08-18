import numpy as np

WIDTH = 20
HEIGHT = 10
EMPTY_CHAR = ' '
HEAD_CHAR = 'X'
BODY_CHAR = 'O'
SNAKE_INIT = [(0,0), (1,0), (2,0), (3,0)]
 
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self, init_body = SNAKE_INIT, init_direction = DOWN):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + position

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

class Apple:
    #class definition
    print()

class Game:

    #Constructor
    def __init__(self, height = HEIGHT, width = WIDTH):
        self.height = height
        self.width = width
        self.snake = Snake()

    def render(self):
        # print(self.height)
        # print(self.width)
        
        #initialize an empty list of lists
        self.board_matrix = np.zeros(shape=(self.height, self.width), dtype = int)

        #print the empty board to the terminal
        
        #print the empty line at the top of the board
        print('+' + self.width * '-' + '+' )

        for i in range(self.height):
            #Add the line at beginning of every row
            print('|', end = '')
            for j in range(self.width):
                #add more code
                if (i, j) in self.snake.body:
                    #print((i,j), self.snake.body)
                    if (i, j) == self.snake.head():
                        #print((i,j), self.snake.head())
                        print(HEAD_CHAR, end ='')
                    else:
                        print(BODY_CHAR, end ='')
                else:
                    print(EMPTY_CHAR, end ='')
            #Add the line at end of every row
            print('|', end ='')
            print()



        #print the empty line at the bottom of the board
        print('+' + self.width * '-' + '+')


#setting up initial direction
initial_direction = SNAKE_INIT

game = Game()
game.render()




