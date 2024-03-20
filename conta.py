class Conta:
    def __init__ (self, nm_conta, saldo, registrar_transacoes):
        self.nm_conta = nm_conta
        self.saldo = saldo
        self.registrar_transacoes = registrar_transacoes
        self.transacoes = []
    
    def depositar(self, valor):
        self.saldo = self.saldo +  valor
        self.registrar_transacoes(f'Depósito de R${valor}')
        
    def sacar(self, valor):
        self.saldo = self.saldo + valor
        self.registrar_transacoes(f'Saque de R${valor}')
        
    def registrar_transacoes(self, descricao):
        self.transacoes.append(descricao)
        
    def exibir_extrato (self):
        print('Extrato da conta: ', self.nm_conta)
        print(' ')
        print('Transações: ')
        print(self.transacoes)
        print(' ')
        print('Saldo atual: R$', self.saldo)

valor = 12  
conta01 = Conta(1, 1.000, " ")
Conta.depositar(valor)