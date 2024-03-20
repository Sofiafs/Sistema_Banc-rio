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

class ContaCorrente(Conta):
    def init(self, num_conta, tipo_conta ='Corrente', saldo = 0):
        super()._init_(num_conta, saldo)
        self.tipo_conta = tipo_conta

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append('Saque: R$ {}'.format(valor))
        else:
            print('Saldo insuficiente para saque.')

class ContaPoupanca(Conta):
    def init(self, num_conta, tipo_conta='Poupança', taxa_juros = 0.02, saldo = 0):
        super().__init__(num_conta, saldo)
        self.tipo_conta = tipo_conta
        self.taxa_juros = taxa_juros

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append('Valor do Saque: R$ {}'.format(valor))
        else:
            print('Saldo insuficiente para saque')

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self.transacoes.append('Juros calculados: R$ {}'.format(juros))

    cliente1 = Cliente('João', '123.456.789-00')

    conta_corrente1 = ContaCorrente('001', 'Corrente')
    cliente1.conta.append(conta_corrente1)

    conta_poupanca1 = ContaPoupanca("002", 'Poupança', 0.03)
    cliente1.contas.append(conta_poupanca1)