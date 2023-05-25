### Declarando Variáveis
cinema = [['|0|' for i in range(10)] for j in range(10)]
opc = ''

### Função Educação, XD!
def bem_vindo():
    print(33*'-')
    print('## SEJA BEM VINDO AO CINEPINHA ##')
    print(33*'-')
    print('\nPossuimos uma grande sala confortável com um total de \n10 filas e 10 poltronas')
    print('\nReserve já seu lugar!!')

### Reserva de Lugar
def reservar():
    poltrona = int(input('Poltrona: '))
    fila = int(input('Fila: '))

    if cinema[poltrona - 1][fila - 1] == '|0|':
        cinema[poltrona - 1][fila - 1] = '(X)'
        print('Poltrona reservada com sucesso!')
    else:
        print('Poltrona já ocupada! Escolha outra.')

### Visualizar a posição da poltrona em relação ao telão
def show_layout():
    print('           * * * TELÃO * * *           ')
    for i in range(10):
        row = ''
        for j in range(10):
            row += cinema[i][j] + ' '
        print(row)

### Funcionamento do Código
bem_vindo()
while opc != '3':
    print('\nSelecione uma opção:')
    print(20*'-')
    print('| 1 | - Reservar')
    print(20*'-')
    print('| 2 |- Layout')
    print(20*'-')
    print('| 3 |- Finalizar')
    print(20*'-')

    opc = input()

    if opc == '1':
        reservar()
    elif opc == '2':
        show_layout()
    elif opc == '3':
        print('Obrigado pela preferência!')
        print('Volte sempre!')  
    else:
        print('Opção inválida! Tente novamente.')
