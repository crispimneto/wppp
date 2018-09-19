#5º)Impressão de números pares de 0 até um número digitado pelo usuário.

limite = int(input('Digite um Valor para Verificação: '))

i = 0
while i <= limite:
    if  i % 2== 0:
        print(i , end=' - ')
    i = i + 1
