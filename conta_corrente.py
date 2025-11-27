from conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, cliente, limite):
        super().__init__(numero_conta, cliente)
        self._limite = limite

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        elif valor > self._saldo + self._limite:
            print("Saldo insuficiente!")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")