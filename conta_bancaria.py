class ContaBancaria:
    def __init__(self, numero_conta, cliente):
        self._numero_conta = numero_conta
        self._cliente = cliente
        self._saldo = 0

    @property
    def saldo(self):
        return self._cliente
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def numero_conta(self):
        return self._numero_conta

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f}")
        else:
            print(f"Valor Inválido!")

    def sacar(self, valor):
        raise NotImplementedError
    
    def exibir_saldo(self):
        print(f"Saldo da conta {self._numero_conta}: R${self._saldo:.2f}")