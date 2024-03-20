from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, num_conta, taxa_juros, saldo):
        super().__init__(num_conta, saldo)
        self.tipo_conta = 'Poupança'
        self.taxa_juros = taxa_juros
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= 0:
            self.saldo -= valor
            self.transacoes.append('Valor do Saque: R$ {}'.format(valor))
            print('Saldo atual: R$', self.saldo)
        else:
            print('Saldo insuficiente para saque')

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self.transacoes.append('Juros calculados: R$ {}'.format(juros))
        print('O resultado foi: R$', juros)
