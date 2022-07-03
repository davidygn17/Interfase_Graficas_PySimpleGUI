import PySimpleGUI as sg


# Criar as Janelas e estilos(layout)


def janela_login():
    sg.theme('reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_pedido():
    sg.theme('reddit')
    [sg.Text('Fazer Pedido')],
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)


# Criar as Janelas Iniciais

janela1, janela2 = janela_login(), None

# Criar um Loop de leitura de eventos

while True:
    window, event, values = sg.read_all_windows()
    # Quando Janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    # Quando queremos ir para proxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma pizza Catupiry c/ Frango')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitados uma Pizza Pepperoni')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitados uma Pizza Catupiry c/ Frango')
    # Quando queremos voltar para janela anterior

# Logica de o que deve acontecer ao clicar os botoes
