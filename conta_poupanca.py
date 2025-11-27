from conta_bancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        elif valor > self._saldo:
            print("Saldo insuficiente!")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def render_juros(self, taxa):
        if taxa > 0:
            juros = self._saldo * taxa
            self._saldo += juros
            print(f"Juros de R${juros:.2f} aplicados!")
        else:
            print("Taxa inválida!")