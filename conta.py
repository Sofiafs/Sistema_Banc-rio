class Conta:
    def __init__(self, nm_conta, saldo):
        self.nm_conta = nm_conta
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f'Depósito de R${valor}')

    def sacar(self, valor):
        self.saldo -= valor
        self.transacoes.append(f'Saque de R${valor}')

    def exibir_extrato(self):
        print('Extrato da conta: ', self.nm_conta)
        print(' ')
        print('Transações: ')
        print(self.transacoes)
        print(' ')
        print('Saldo atual: R$', self.saldo)

valor = 12
conta01 = Conta(1, 1000)
Conta.sacar(conta01, valor)
Conta.depositar(conta01, valor)
Conta.exibir_extrato(conta01)