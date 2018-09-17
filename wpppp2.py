#2°) Escreva um programa que leia três números e que imprima o maior e o meno.

nr1 = int(input('Digite o Primeiro Número: '))
nr2 = int(input('Digite o Segundo Número: '))
nr3 = int(input('Digite o Terceiro Número: '))

menor = nr1
maior = nr1

if nr2 < nr1 and nr2 < nr3:
    menor = nr2
if nr3 < nr2 and nr3 < nr1:
    menor = nr3
print(f'O menor valor é: {menor}')

if nr2 > nr1 and nr2 > nr3:
    maior = nr2
if nr3 > nr2 and nr3 > nr1:
    maior = nr3
    
print(f'O maior valor é: {maior}')  