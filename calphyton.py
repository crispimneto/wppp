def soma(nr1,nr2):
    return(nr1+nr2)

def mult(nr1,nr2):
    return(nr1*nr2)

def sub(nr1,nr2):
    return(nr1-nr2)

def div(nr1,nr2):
    return(nr1/nr2)

def menu():
    print ('='* 44)
    print ('| 1 = SOMA' + '                  ' + '6 = NOVA OPÇÃO |')
    print ('| 2 = SUBTRAÇÃO' + '             ' + '7 = NOVA OPÇÃO |')
    print ('| 3 = DIVISÃO'  +'               ' + '8 = NOVA OPÇÃO |')
    print ('| 4 = DIVISÃO'  +'               ' + '9 = NOVA OPÇÃO |')
    print ('| 5 = RAIZ QUADRADA' + '         ' + '0 = SAIR       |')
    print ('=' * 44)
    

print(menu())

menu = int(input('Digite uma Opção: ZERO para Sair: '))

while menu != 0:
    
    if menu == 1:
        vlr1 = int(input('Digite o Primeivo Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        print('A Soma é = ' , soma(vlr1,vlr2))
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 2:
        vlr1 = int(input('Digite o Primeivo Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        print('A Subtração é = ', sub(vlr1,vlr2))
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 3:
        vlr1 = int(input('Digite o Primeivo Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        print('A Multiplicação é = ', mult(vlr1,vlr2))
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 4:
        vlr1 = int(input('Digite o Primeivo Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        while vlr2 == 0:
            print('O Valor não pode ser ZERO - Redigite: ')
            vlr2 = int(input('Digite o Segundo Valor: '))
        print(f'A Divisão é =  {div(vlr1,vlr2):.2f}')
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    else:
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
        