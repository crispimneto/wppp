#4°) Escreva um programa que pergunte a distância que um passageiro deseja percorre em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

dist = int(input('Digite a Distância em KM a ser percorrida: '))

if dist <= 200:
    print(f'O Valor da Passagem é R$ {dist * .50:.2f}')
else:
    print(f'O Valor da Passagem é R$ {dist *.45:.2f}')
