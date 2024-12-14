import PySimpleGUI as sg

BOX_SIZE = (40, 40)


def gui():

    layout = []
    topY = 40
    bottomY = 0
    for r in range(16):
        leftX = 0
        rightX = 40
        row = []
        for c in range(16):
            row.append(sg.Graph(BOX_SIZE, (leftX, bottomY), (bottomY, topY), background_color='black', key=(r, c)))
            rightX += 40
            leftX += 40
        topY -= 40
        bottomY -= 40
        layout.append(row)

    window = sg.Window('Snake game', layout)

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
    window.close()
