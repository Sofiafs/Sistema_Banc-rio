class ContaCorrente:
    def init(self, num_conta, tipo_conta ='Corrente', saldo = 0):
        super()._init_(num_conta, saldo)
        self.tipo_conta = tipo_conta

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append('Saque: R$ {}'.format(valor))
        else:
            print('Saldo insuficiente para saque.')