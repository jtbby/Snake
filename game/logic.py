import pynput
from pynput import keyboard
from pynput.keyboard import Key
import time


# Create the board
# Find random middle spot for snake
# Find random spot for food

# 0 is unoccupied
# 1 is snake
# 2 is food

class gameBoard:
    def __init__(self):
        self.board = [[0] * 20 for i in range(20)]
        self.direction = 'r'
        self.board[9][5] = 1  # Start the snake in the middle of the board
        self.snakeHead = (9, 5)
        self.snakeTail = None
        self.lastMovement = time.time()

    # Automatically move snake if no key pressed within .5s
    # Move otherwise
    def moveSnake(self):
        if self.direction == 'r':
            x, y = self.snakeHead
            self.snakeHead = (x, y + 1)
            self.board[x][y] = 0
            self.board[x][y + 1] = 1

        elif self.direction == 'l':
            x, y = self.snakeHead
            self.snakeHead = (x, y - 1)
            self.board[x][y] = 0
            self.board[x][y - 1] = 1

        elif self.direction == 'u':
            x, y = self.snakeHead
            self.snakeHead = (x - 1, y)
            self.board[x][y] = 0
            self.board[x - 1][y] = 1
            self.board[x][y] = 0

        elif self.direction == 'd':
            x, y = self.snakeHead
            self.snakeHead = (x + 1, y)
            self.board[x][y] = 0
            self.board[x + 1][y] = 1
            self.board[x][y] = 0

        self.lastMovement = time.time()

    def directionChange(self, key):
        if key == Key.right:
            self.direction = 'r'
        elif key == Key.left:
            self.direction = 'l'
        elif key == Key.up:
            self.direction = 'u'
        elif key == Key.down:
            self.direction = 'd'


def listen(game):
    def on_key_press(key):
        try:
            game.directionChange(key)
        except AttributeError:
            pass

    # Create a new listener
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
