import pynput
from pynput import keyboard
from pynput.keyboard import Key
import time
import random


# Create the board
# Find random middle spot for snake
# Find random spot for food

# 0 is unoccupied
# 1 is snake
# 2 is food


#  NOTE ONCE THE SNAKE HAS EATEN THE APPLE, KEEP THE TAIL IN THE SAME SPOT
class gameBoard:
    def __init__(self):
        self.board = [[0] * 20 for i in range(20)]
        self.direction = 'r'
        self.board[9][5] = 1  # Start the snake in the middle of the board
        self.snakeHead = (9, 5)
        self.snakeTail = (9, 5)
        self.lastMovement = time.time()
        self.placeApple()

    # Automatically move snake if no key pressed within .5s
    # Move otherwise
    def moveSnake(self):
        x, y = self.snakeHead
        tailX, tailY = self.snakeTail
        ate = False
        if self.direction == 'r':
            self.snakeHead = (x, y + 1)
            ate = self.checkEating(x, y + 1)
            self.board[x][y + 1] = 1

        elif self.direction == 'l':
            self.snakeHead = (x, y - 1)
            ate = self.checkEating(x, y - 1)
            self.board[x][y - 1] = 1

        elif self.direction == 'u':
            self.snakeHead = (x - 1, y)
            ate = self.checkEating(x - 1, y)
            self.board[x - 1][y] = 1

        elif self.direction == 'd':
            self.snakeHead = (x + 1, y)
            ate = self.checkEating(x + 1, y)
            self.board[x + 1][y] = 1

        if not ate:
            self.board[tailX][tailY] = 0
            self.snakeTail = ()

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

    def placeApple(self):

        while True:
            r = random.randint(0, 19)
            c = random.randint(0, 19)
            if self.board[r][c] == 0:
                break
        self.board[r][c] = 2

    def checkEating(self, x, y):
        if self.board[x][y] == 2:
            self.placeApple()
            return True
        return False


def listen(game):
    def on_key_press(key):
        try:
            game.directionChange(key)
        except AttributeError:
            pass

    # Create a new listener
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
