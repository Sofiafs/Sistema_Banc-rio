class Cliente:
    def __init__(self,nome , cpf , contas_ass):
        self.nome = nome
        self.cpf = cpf
        self.contas_ass = contas_ass
    
print ('Bem vindo ao Sistema de Gerenciamento Bancário!')
print (" ")
print ('Menu:')
print ("1- Criação de clientes")
print ("2- Poupança")
op = str(input("Digite a operação: "))

if op == "1":
    n = str(input('Digite seu nome: '))
    c = int(input("Digite seu cpf: "))
    ca = str(input("Digite as contas associadas: "))
    print('Criação de conta concluida.')
elif op == "2":
    n = str(input('Digite seu nome: '))
    c = int(input("Digite seu cpf: "))
    ca = str(input("Digite as contas associadas: "))
    tp = str(input("Digite o tipo de conta: "))
    tx = float(input("Digite a taxa de juros: "))
    print("Poupança criada com sucesso.")
else:
    print("Inválido.")