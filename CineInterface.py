### Primeira implementação de uma Interface Gráfica
### -Henrique Pinheiro

from tkinter import *

### criando a janela principal(jan) 
jan = Tk()
jan.title('PinhaCine')
jan.geometry('300x400')
###------------------------------------

### declarando variáveis
cinema = [['|0|' for i in range(10)] for j in range(10)]
opc = ''
###------------------------------------

### Função Bem Vindo (educação é sempre bom né, XD)
def bem_vindo():
    bemvindo_lb1 = Label(jan, text= 'ºº SEJA BEM-VINDO AO PINHACINE ºº')
    bemvindo_lb1.pack(padx=10, pady=10)
    bemvindo_lb1 = Label(jan, text= 'OFERECEMOS UMA SALA CONFORTAVEL \nCOM 10 FILAS E 10 POLTRONAS')
    bemvindo_lb1.pack(padx=5, pady=5)
    bemvindo_lb1 = Label(jan, text= 'ºRESERVE SUA POLTRONAº')
    bemvindo_lb1.pack()
###------------------------------------

### Função Reservar(botão de reservar)
def reservar():
    ### Função Confirmar (janela para inserir poltrona e fila desejadas)
    def confirma():
        poltrona = int(poltrona_entry.get())
        fila = int(fila_entry.get())

        if cinema[poltrona - 1][fila - 1] == '|0|':
            cinema[poltrona - 1][fila - 1] = '(X)'
            result_label.config(text='Poltrona reservada com sucesso!')
        else:
            result_label.config(text='Poltrona já ocupada! Escolha outra.')

    reserva_window = Toplevel(jan)
    reserva_window.title('Reserva de Poltrona')

    poltrona_label = Label(reserva_window, text='Poltrona:')
    poltrona_label.grid(row=0, column=0, padx=5, pady=5)

    poltrona_entry = Entry(reserva_window)
    poltrona_entry.grid(row=0, column=1, padx=5, pady=5)

    fila_label = Label(reserva_window, text='Fileira:')
    fila_label.grid(row=1, column=0, padx=5, pady=5)

    fila_entry = Entry(reserva_window)
    fila_entry.grid(row=1, column=1, padx=5, pady=5)

    confirm_button = Button(reserva_window, text='Confirmar', command=confirma)
    confirm_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    result_label = Label(reserva_window, text='')
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    ###------------------------------------
###------------------------------------

### Função Layout (visualizar a posição da poltrona dentro da sala)
def show_layout():
    layout_window = Toplevel(jan)
    layout_window.title('Layout da Sala')

    tela_label = Label(layout_window, text='* * * TELÃO * * *')
    tela_label.pack(padx=10, pady=10)

    for i in range(10):
        row_frame = Frame(layout_window)
        
        for j in range(10):
            poltrona_label = Label(row_frame, text=cinema[i][j])
            poltrona_label.pack(side=LEFT, padx=2, pady=2)

        row_frame.pack()
###------------------------------------

### Funcionamento da Janela Principal(jan)
bem_vindo()
while opc != '3':
    opt_label = Label(jan, text='\nSelecione uma opção:')
    opt_label.pack(padx=10, pady=10)

    reserva_button = Button(jan, text='1 - Reservar', command=reservar)
    reserva_button.pack(padx=10, pady=5)

    layout_button = Button(jan, text='2 - Layout', command=show_layout)
    layout_button.pack(padx=10, pady=5)
    
    goodbye_label = Label(jan, text='°°°OBRIGADO PELA PREFERENCIA°°°\n°°VOLTE SEMPRE°°')
    goodbye_label.pack(padx=10, pady=5)
    sair_button = Button(jan, text='3 - Finalizar', command=quit)
    sair_button.pack(padx=10, pady=5)

    opc = input()
###------------------------------------
