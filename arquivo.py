#Cria o arquivo em modo ESCRITA
criar = opem("presenca.txt","w")
criar.close()

#Cria funções para ESCRITA e LEITURA de uma lista de presença
#1ª Função adiciona nome de aluno

def adicionar_aluno():
    "O Nome do aluno deve estar entre parenteses"
    #cria a variavel para editar o nome do aluno
    aluno = input("Qual o nome no aluno? \n")
    escrever = open("presenca.txt","a")
    escrever.write(aluno+ "\n")
    escrever.close()
    
#2ª Função para LER os nomes na Lista

def aluno_presente():
    "Deve ser declarado um inteiro correspondente a linha em que o aluno está"
    #cria a variavel para ler o nome do aluno
    leitura = open("presenca.txt","r")
    ler = leitura.readlines()
    print (ler[1:5])
    aluno = input("Deseja saber todos os presentes? s/n \n")
    if aluno == "s":
        for nomes in ler:
            print(nomes)
            elif aluno == "n":
            qual_aluno = input("Qual Nr do Aluno? \n")
            print ler [qual_aluno-1]
    else:
                print "ERRO, Digite s ou n"
    
    