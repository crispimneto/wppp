# Estudo de Operações matemáticas em Python
# Calculadora com algumas operações básicas
# João Crispim Neto - 17 de setembro de 2018

# Definição das funções básicas para os cálculos.
import math

def soma(nr1,nr2):
    return(nr1+nr2)

def mult(nr1,nr2):
    return(nr1*nr2)

def sub(nr1,nr2):
    return(nr1-nr2)

def div(nr1,nr2):
    return(nr1/nr2)

# Função que gera o Menu inicial.
def menu():
    print ('='* 44)
    print ('| 1 = SOMA' + '                  ' + '6 = NOVA OPÇÃO |')
    print ('| 2 = SUBTRAÇÃO' + '             ' + '7 = NOVA OPÇÃO |')
    print ('| 3 = MULTIPLICAÇÃO'  +'         ' + '8 = NOVA OPÇÃO |')
    print ('| 4 = DIVISÃO'  +'               ' + '9 = NOVA OPÇÃO |')
    print ('| 5 = RAIZ QUADRADA' + '         ' + '0 = SAIR       |')
    print ('=' * 44)
    
# Inicializa o Menu
print(menu())

menu = int(input('Digite uma Opção: ZERO para Sair: '))

#Entra em loop até que seja digitado ZERO para encerrar.
while menu != 0:
    
    if menu == 1:
        vlr1 = int(input('Digite o Primeiro Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        print('A Soma é = ' , soma(vlr1,vlr2))
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 2:
        vlr1 = int(input('Digite o Primeiro Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        print('A Subtração é = ', sub(vlr1,vlr2))
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 3:
        vlr1 = int(input('Digite o Primeiro Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        print('A Multiplicação é = ', mult(vlr1,vlr2))
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 4:
        vlr1 = int(input('Digite o Primeiro Valor: '))
        vlr2 = int(input('Digite o Segundo Valor: '))
        while vlr2 == 0:
            print('O Valor não pode ser ZERO - Redigite: ')
            vlr2 = int(input('Digite o Segundo Valor: '))
        print(f'A Divisão é =  {div(vlr1,vlr2):.2f}')
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 5:
        vlr1 = int(input('Digite o Valor para Calculo da Raiz Quadrada: '))
        print (f'A raiz de {vlr1} é igual a {(math.sqrt(vlr1)):.2f}')
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 6:
        print('Opção ainda nao Implementada')
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 7:
        print('Opção ainda nao Implementada')
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 8:
        print('Opção ainda nao Implementada')
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    elif menu == 9:
        print('Opção ainda nao Implementada')
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
    else:
        menu = int(input('Digite uma Opção: ZERO para Sair: '))
        