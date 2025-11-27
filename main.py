from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

def main():
    print("\n- - BEM-VINDO AO EASYBANK - - ")

    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    email = input("Digite o E-mail: ")
    cliente = Cliente(nome, cpf, email)
    print(f"\nCliente cadastrado:\n{cliente.exibir_dados()}")

    conta_tipo = ""
    while conta_tipo not in ["corrente", "poupanca"]:
        print("\nESCOLHA O TIPO DE CONTA PARA ABRIR")
        print("[1] - Corrente")
        print("[2] - Poupança")
        escolha = input("Digite 1 ou 2: ")
        if escolha == "1":
            conta_tipo = "corrente"
        elif escolha == "2":
            conta_tipo = "poupanca"
        else:
            print("Opção Inválida!")

    numero_conta = input("Digite o número da conta: ")

    if conta_tipo == "corrente":
        valor_valido = False
        while not valor_valido:
            try:
                limite = float(input("Digite o limite da Conta Corrente: "))
                if limite >= 0:
                    valor_valido = True
                else:
                    print("Limite não pode ser negativo.")
            except ValueError:
                print("Valor Inválido!")
        conta = ContaCorrente(numero_conta, cliente, limite)
        print("\nConta Corrente criada com Sucesso!")
    else:
        conta = ContaPoupanca(numero_conta, cliente)
        print("\nConta Poupança criada com Sucesso!")

    while True:
        print("\nEscolha a operação")
        print("1 - Depositar")
        print("2 - Sacar")
        if conta_tipo == "corrente":
            print("3 - Saldo")
            print("0 - SAIR")
        else:
            print("3 - Render juros")
            print("4 - Saldo")
            print("0 - SAIR")

        opcao = input("Opção: ")

        if opcao == "1":
            valor_valido = False
            while not valor_valido:
                try:
                    valor = float(input("Digite o valor do depósito: "))
                    if valor > 0:
                        valor_valido = True
                    else:
                        print("O valor deve ser positivo.")
                except ValueError:
                    print("Valor inválido. Digite um número.")
            conta.depositar(valor)
        elif opcao == "2":
            valor_valido = False
            while not valor_valido:
                try:
                    valor = float(input("Digite o valor do saque: "))
                    if valor > 0:
                        valor_valido = True
                    else:
                        print("O valor deve ser positivo.")
                except ValueError:
                    print("Valor inválido. Digite um número.")
            conta.sacar(valor)
        elif conta_tipo == "corrente" and opcao == "3":
            conta.exibir_saldo()
        elif conta_tipo == "poupanca" and opcao == "3":
            taxa_valida = False
            while not taxa_valida:
                try:
                    taxa = float(input("Digite a taxa de juros (ex: 0.10 = 10%): "))
                    if taxa >= 0:
                        taxa_valida = True
                    else:
                        print("A taxa não pode ser negativa.")
                except ValueError:
                    print("Valor inválido. Digite um número.")
            conta.render_juros(taxa)
        elif conta_tipo == "poupanca" and opcao == "4":
            conta.exibir_saldo()
        elif opcao == "0":
            print("\nObrigado por usar o EasyBank! Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()