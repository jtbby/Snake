import PySimpleGUI as sg

BOX_SIZE = (35, 35)


def gui():
    sg.popup("Welcome to the snake game press 'ok' to start")

    sg.theme('Dark Grey 4')
    layout = []
    for r in range(20):
        row = []
        for c in range(20):
            row.append(sg.Graph(BOX_SIZE, (0, 0), (0, 0), background_color='black', key=(r, c), pad=(1, 1)))
        layout.append(row)

    window = sg.Window('Snake game', layout)

    while True:

        event, values = window.read(timeout=10)

        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break

        window[(0, 0)].update(background_color='red')

    window.close()
