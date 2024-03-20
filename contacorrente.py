from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, num_conta, saldo):
        super().__init__(num_conta, saldo)
        self.tipo_conta = 'Corrente'
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo > 0:
            self.saldo -= valor
            self.transacoes.append('Saque: R$ {}'.format(valor))
            print('Saldo concluido com sucesso!')
            print('Saldo atual: R$', self.saldo)
        else:
            print('Saldo insuficiente para saque.')