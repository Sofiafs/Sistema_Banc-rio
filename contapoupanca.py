class ContaPoupanca:
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

    cliente1 = ('João', '123.456.789-00')

    conta_corrente1 = ('001', 'Corrente')
    cliente1.conta.append(conta_corrente1)

    conta_poupanca1 = ("002", 'Poupança', 0.03)
    cliente1.contas.append(conta_poupanca1)