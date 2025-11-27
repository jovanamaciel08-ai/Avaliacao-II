class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_dados(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nE-mail: {self.email}"