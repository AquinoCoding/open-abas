import PySimpleGUI as sg


class Interface:
    def __init__(self):

        self.sg = sg

        self.informationPassword = {
            'sgoAcess': ['.', '@'],
            'linkedin': ['@gmail.com', ''],
            'email': ['.@.com.br', ''],
        }

    def main(self):

        sg = self.sg

        self.informationPass = {
            'Sgo': False,
            'Linkedin': False,
            'Rocket': False,
            'Email': False,
            'Youtube': False
        }

        sg.SetOptions(background_color='#363636',
                      text_element_background_color='#363636',
                      element_background_color='#363636',
                      scrollbar_color=None,
                      input_elements_background_color='#F7F3EC',
                      button_color=('white', '#4F4F4F'))

        CheckBoxSelect = [
            [sg.Text('Informe o que deseja Abrir\n')],
            [
                sg.Checkbox('SGO', key='KEY_Sgo'),
                sg.Checkbox('Linkedin', key='KEY_Linke'),
                sg.Checkbox('Rocket', key='KEY_Rocket'),
                sg.Checkbox('Youtube', key='KEY_Youtube'),
                sg.Checkbox('Email', key='KEY_Email'),
            ],
        ]
        AlterSelect = [
            [
                sg.Button('Alterar', key='KEY_AlSgo'),
                sg.Button('Alterar', key='KEY_AlLink'),
                sg.Button('Alterar'),
                sg.Button('Alterar'),
                sg.Button('Alterar', key='KEY_AlEmail'),
            ],
        ]

        layoutButton = [[sg.Text('\n')],
                        [
                            sg.Button('Iniciar',
                                      size=(15, 2),
                                      key='SendRequest')
                        ]]

        layout = [[sg.Column(CheckBoxSelect, element_justification='center')],
                  [sg.Column(AlterSelect, element_justification='center')],
                  [sg.Column(layoutButton, element_justification='center')]]

        window = sg.Window('Assistente',
                           layout,
                           size=(600, 400),
                           element_justification='center')
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if 'KEY_AlSgo' == event:
                print('sgoAcess')
                self.informationPassword = self.AcessAlt('sgoAcess')

            if 'KEY_AlLink' == event:
                print('linkedin')
                self.informationPassword = self.AcessAlt('linkedin')

            if 'KEY_AlEmail' == event:
                print('email')
                self.informationPassword = self.AcessAlt('email')

            if event == 'SendRequest':
                break

            if values['KEY_Sgo'] == True:
                self.informationPass = {**informationPass, 'Sgo': True}

            if values['KEY_Linke'] == True:
                self.informationPass = {**informationPass, 'Linkedin': True}

            if values['KEY_Rocket'] == True:
                self.informationPass = {**informationPass, 'Rocket': True}

            if values['KEY_Email'] == True:
                self.informationPass = {**informationPass, 'Email': True}

            if values['KEY_Youtube'] == True:
                self.informationPass = {**informationPass, 'Youtube': True}

        return informationPass, informationPassword

    def AcessAlt(self, validationAlt):

        informationPassword = self.informationPassword
        sg = self.sg

        sg.SetOptions(background_color='#363636',
                      text_element_background_color='#363636',
                      element_background_color='#363636',
                      scrollbar_color=None,
                      input_elements_background_color='#F7F3EC',
                      button_color=('white', '#4F4F4F'))

        print(informationPassword)

        login = [
            [sg.Text('Alteração de Acesso\n')],
            [sg.Text('Login '),
             sg.Input(key='KEY_login', size=(20, 0))],
            [
                sg.Text('Senha'),
                sg.Input(key='KEY_password', password_char='*', size=(20, 0))
            ],
        ]
        button = [[
            sg.Button('Confirmar', key='KEY_Confirm', size=(10, 0)),
            sg.Button('Cancelar', key='KEY_Cancelar', size=(7, 0))
        ]]

        layout = [[sg.Column(login, element_justification='center')],
                  [sg.Column(button, element_justification='center')]],

        window = sg.Window('Acesso',
                           layout,
                           element_justification='center',
                           size=(300, 200))

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if 'KEY_Confirm' == event:
                self.informationPassword = {
                    **informationPassword, validationAlt:
                    [values['KEY_login'], values['KEY_password']]
                }
                window.close()

            if 'KEY_Cancelar' == event:
                break

            return informationPassword


iniciaBoot = Interface()
iniciaBoot.main()
