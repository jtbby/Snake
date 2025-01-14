import time

import PySimpleGUI as sg
import logic
from logic import listen
from game.logic import gameBoard
import threading

BOX_SIZE = (35, 35)


def gui():
    sg.popup("Welcome to the snake game press 'ok' to start")
    sg.theme('Dark Grey 4')

    while True:
        layout = [[sg.Text("Score: ", font=("Calibri", 20))]]
        for r in range(20):
            row = []
            for c in range(20):
                row.append(sg.Graph(BOX_SIZE, (0, -40), (35, -5), background_color='black', key=(r, c), pad=(1, 1)))
            layout.append(row)

        game = gameBoard()
        listen(game)
        board = game.board

        window = sg.Window('Snake game', layout)

        while True:

            event, values = window.read(timeout=1)

            if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
                break

            updateBoard(window, board)
            layout[0][0].update(value="Score: " + str(game.score))

            #  To control the game timing
            currentTime = time.time()
            if currentTime - game.lastMovement >= 0.175:
                gameOver = game.moveSnake()

                if gameOver:
                    window.close()
                    retry = sg.popup_yes_no(f"Game Over! Your score is {game.score}. Do you want to retry?",
                                            title="Game Over")
                    if retry == "Yes":
                        break
                    else:
                        return

        window.close()


#  function to redraw the board asap
def updateBoard(window, board):
    for r in range(20):
        for c in range(20):
            if board[r][c] == 1:
                window[(r, c)].update(background_color='green')
            elif board[r][c] == 2:
                window[(r, c)].update(background_color='red')
            else:
                window[(r, c)].update(background_color='black')
