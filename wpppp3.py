#3º) Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
#Para salário superiores R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, de 15%.

sal = float(input('Digite o Salário Base: '))

if sal > 1250.00:
    #aumento = (sal * .10)
    print(f'A Correção foi de R$ {(sal * .10):.2f}')
else:
    #aumento = (sal * .15)
    print (f'A Correlçao foi de R$ {(sal * .15):.2f}')