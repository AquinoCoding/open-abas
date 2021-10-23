import PySimpleGUI as sg


def init00():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text('Informe o que deseja Abrir')],
        [sg.Checkbox(' SGO    ', key='KEY_SGO'),
         sg.Checkbox(' Linkedin ')],
        [sg.Checkbox('Rocket '),
         sg.Checkbox(' Facebook ')],
        [sg.Checkbox(' Youtube'),
         sg.Checkbox(' Instagram')],
    ]

    # Create the Window
    window = sg.Window('Assistente',
                       layout,
                       size=(600, 400),
                       element_justification='center')
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        elif values['KEY_SGO'] == True:
            print('True')

        print('You entered ', values[0])
