#5º)Impressão de números pares de 0 até um número digitado pelo usuário.

limite = int(input('Digite um Valor para Verificação: '))

for x in range (0, limite+1):
    if x % 2 == 0:
        print ( x , end=' - ')
    x = x + 1