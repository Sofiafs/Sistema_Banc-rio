import conta
import cliente
import contacorrente
import contapoupanca



print ('Bem vindo ao Sistema de Gerenciamento Bancário!')
print (" ")
n = str(input('Digite o nome do cliente: '))
cer = int(input('Digite o número do CPF do cliente: '))
cliente01 = cliente.Cliente(n, cer)

# conta01 = contacorrente.ContaCorrente(1, 1000)
# contacorrente.ContaCorrente(conta01, valor)

# conta02 = contapoupanca.ContaPoupanca(2, 0.02, 1000)
# contapoupanca.ContaPoupanca.calcular_juros(conta02)

# conta03 = conta.Conta(3, 1000)
# conta.Conta.depositar(conta03, valor)

# conta04 = conta.Conta(4, 1000)
# conta.Conta.sacar(conta04, valor)

# conta.Conta.exibir_extrato(conta03)

