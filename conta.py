class Conta:
    def __init__(self, nm_conta, saldo):
        self.nm_conta = nm_conta
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f'Depósito de R${valor}')
        print('Saldo atual: R$', self.saldo)

    def sacar(self, valor):
        self.saldo -= valor
        self.transacoes.append(f'Saque de R${valor}')
        print('Saldo atual: R$', self.saldo)

    def exibir_extrato(self):
        print('Extrato da conta: ', self.nm_conta)
        print(' ')
        print('Transações: ')
        print(self.transacoes)
        print(' ')
        print('Saldo atual: R$', self.saldo)