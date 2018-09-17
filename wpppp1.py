#1º) Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso utrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nessa caso, exiba o valor da multa, cobrando R$5,00 por km acima de 80.

vel = int(input('Digite a Velocidade do seu Veículo: '))

if vel > 80:
    print(f'Você foi Multado em R$ {((vel-80)*5):.2f}')
else:
    print('Velocidade Correta')
    
