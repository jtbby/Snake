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
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None


#  NOTE ONCE THE SNAKE HAS EATEN THE APPLE, KEEP THE TAIL IN THE SAME SPOT
class gameBoard:
    def __init__(self):
        self.board = [[0] * 20 for i in range(20)]
        self.direction = 'r'
        self.board[9][5] = 1  # Start the snake in the middle of the board
        self.snakeHead = Node(9, 5)
        self.snakeTail = self.snakeHead
        self.lastMovement = time.time()
        self.placeApple()

    # Automatically move snake if no key pressed within .5s
    # Move otherwise
    def moveSnake(self):
        x, y = self.snakeHead.x, self.snakeHead.y
        ate = False
        if self.direction == 'r':
            ate = self.checkEating(x, y + 1)
            newX, newY = x, y + 1

        elif self.direction == 'l':
            ate = self.checkEating(x, y - 1)
            newX, newY = x, y - 1

        elif self.direction == 'u':
            ate = self.checkEating(x - 1, y)
            newX, newY = x - 1, y

        elif self.direction == 'd':
            ate = self.checkEating(x + 1, y)
            newX, newY = x + 1, y

        self.board[newX][newY] = 1
        self.snakeHead.next = Node(newX, newY)
        self.snakeHead = self.snakeHead.next

        if not ate: # move the snake
            self.moveSnakeBody()

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

    def moveSnakeBody(self):
        old = self.snakeTail
        self.board[old.x][old.y] = 0
        self.snakeTail = self.snakeTail.next
        old.next = None
        curr = self.snakeTail


def listen(game):
    def on_key_press(key):
        try:
            game.directionChange(key)
        except AttributeError:
            pass

    # Create a new listener
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
