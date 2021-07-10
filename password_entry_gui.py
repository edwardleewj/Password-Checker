import PySimpleGUI as sg

from checkmypass import main

sg.theme('BlueMono')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter Password to check: '), sg.InputText(password_char='*')],
          [sg.Button('Check', bind_return_key=True), sg.Button('Exit')]]

# Create the Window
window = sg.Window('Password Checker', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks exit
        break
    else:
        message = main(values[0])
        layout2 = [[sg.Text(message)],
                   [sg.Button('Exit', bind_return_key=True)]]
        window2 = sg.Window('Results of Check', layout2)
        while True:
            event2, values2 = window2.read()
            if event2 == sg.WIN_CLOSED or event2 == 'Exit':  # if user closes window or clicks exit
                break
    window2.close()
    window.FindElement(0).update('')
window.close()
