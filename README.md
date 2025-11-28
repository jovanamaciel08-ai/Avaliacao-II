# 🏦 EasyBank - Sistema de Gerenciamento de Contas Bancárias

## 📋 Descrição da Atividade

Este projeto implementa um **sistema bancário orientado a objetos** que demonstra o uso de **herança**, **encapsulamento** e **polimorfismo** em Python. A EasyBank está ampliando sua plataforma oferecendo novos tipos de contas com regras específicas, permitindo que clientes gerenciem tanto contas correntes quanto poupanças.

---

## 🎯 Objetivos da Atividade

- ✅ Criar uma hierarquia de classes bem estruturada
- ✅ Implementar encapsulamento para proteger dados sensíveis
- ✅ Utilizar herança para reutilizar código
- ✅ Aplicar polimorfismo para diferentes tipos de saques
- ✅ Validar operações bancárias
- ✅ Facilitar futuras expansões do sistema

---

## 🏗️ Arquitetura do Sistema

### Hierarquia de Classes

```
Cliente
├── ContaBancaria (classe base abstrata)
│   ├── ContaCorrente (com limite especial)
│   └── ContaPoupanca (com rendimento automático)
```

---

## 📚 Descrição das Classes

### 1️⃣ **Cliente** (`cliente.py`)

Representa um cliente do banco com suas informações pessoais.

**Atributos:**
- `nome` (str): Nome completo do cliente
- `cpf` (str): CPF do cliente
- `email` (str): Email para contato

**Métodos:**
- `exibir_dados()`: Retorna uma string formatada com as informações do cliente

**Exemplo de Uso:**
```python
cliente = Cliente("João Silva", "123.456.789-00", "joao@email.com")
print(cliente.exibir_dados())
# Saída:
# Nome: João Silva
# CPF: 123.456.789-00
# E-mail: joao@email.com
```

---

### 2️⃣ **ContaBancaria** (`conta_bancaria.py`)

Classe base que define a estrutura comum de todas as contas bancárias. Implementa **encapsulamento** protegendo dados críticos.

**Atributos Protegidos:**
- `_numero_conta` (str): Número único da conta
- `_cliente` (Cliente): Objeto Cliente associado à conta
- `_saldo` (float): Saldo da conta (inicia em 0)

**Propriedades (Properties):**
- `saldo`: Retorna o saldo atual (getter protegido)
- `cliente`: Retorna o cliente associado
- `numero_conta`: Retorna o número da conta

**Métodos:**
- `depositar(valor)`: Adiciona um valor positivo ao saldo
  - Valida se o valor é positivo
  - Exibe mensagem de sucesso ou erro
  
- `sacar(valor)`: Método polimórfico que será redefinido nas subclasses
  - Levanta `NotImplementedError`
  
- `exibir_saldo()`: Exibe o saldo formatado em moeda

**Exemplo de Uso:**
```python
conta = ContaBancaria("001", cliente)
conta.depositar(1000)  # Depósito de R$1000.00
conta.exibir_saldo()   # Saldo da conta 001: R$1000.00
```

---

### 3️⃣ **ContaCorrente** (`conta_corrente.py`)

Subclasse que herda de `ContaBancaria` e implementa conta corrente com limite especial.

**Características:**
- ✅ Permite saques acima do saldo, desde que não ultrapasse o limite
- ✅ Limite especial definido no construtor
- ✅ Maior flexibilidade para o cliente

**Atributos:**
- `_limite` (float): Limite especial disponível na conta

**Métodos Herdados:**
- `depositar(valor)`
- `exibir_saldo()`

**Métodos Sobrescritos:**
- `sacar(valor)`: Implementa lógica de saque com limite

**Lógica do Saque:**
```
Saldo disponível = saldo atual + limite
Saque permitido se: valor <= (saldo + limite)
```

**Exemplo de Uso:**
```python
conta_corrente = ContaCorrente("12345", cliente, limite=500)
conta_corrente.depositar(1000)      # Saldo: R$1000.00
conta_corrente.sacar(1200)          # Permitido (saldo + limite = 1500)
# Saque de R$1200.00 realizado com sucesso!
conta_corrente.exibir_saldo()       # Saldo da conta 12345: R$-200.00
```

---

### 4️⃣ **ContaPoupanca** (`conta_poupanca.py`)

Subclasse que herda de `ContaBancaria` e implementa conta poupança com rendimento automático.

**Características:**
- ❌ Não possui limite especial
- ✅ Saque não pode deixar saldo negativo
- ✅ Possibilidade de render juros sobre o saldo
- ✅ Ideal para poupar e ganhar rendimento

**Métodos Herdados:**
- `depositar(valor)`
- `exibir_saldo()`

**Métodos Sobrescritos:**
- `sacar(valor)`: Implementa lógica de saque sem limite

**Métodos Adicionais:**
- `render_juros(taxa)`: Aplica juros sobre o saldo
  - Parâmetro `taxa`: Taxa decimal (ex: 0.10 = 10%)
  - Valida se a taxa é positiva
  - Calcula juros como: `juros = saldo * taxa`

**Lógica do Saque:**
```
Saque permitido se: valor > 0 E valor <= saldo
```

**Exemplo de Uso:**
```python
conta_poupanca = ContaPoupanca("67890", cliente)
conta_poupanca.depositar(5000)      # Saldo: R$5000.00
conta_poupanca.render_juros(0.10)   # Aplica 10% de juros
# Juros de R$500.00 aplicados!
# Saldo: R$5500.00
conta_poupanca.sacar(1000)          # Permitido
# Saque de R$1000.00 realizado com sucesso!
```

---

## 🔒 Regras Gerais do Sistema

| Regra | Descrição |
|-------|-----------|
| 🔐 Encapsulamento | Saldo, cliente e número da conta são protegidos (private/protected) |
| 💰 Validação de Valor | Apenas valores positivos são aceitos em depósitos e saques |
| ❌ Saldo Negativo | Contas Poupança não podem ter saldo negativo; Contas Correntes podem (até o limite) |
| 🏦 Limite Especial | Apenas Contas Correntes possuem limite |
| 📈 Rendimento | Apenas Contas Poupança renderizam juros |

---

## 🎮 Cenário de Teste (`main.py`)

O arquivo `main.py` implementa um **menu interativo** que permite testar todas as funcionalidades:

### Fluxo do Programa:

1. **Boas-vindas** e cadastro do cliente
   - Solicita: nome, CPF e email
   - Exibe dados do cliente

2. **Escolha do tipo de conta**
   - Conta Corrente ou Conta Poupança
   - Se Corrente, define o limite

3. **Menu de operações**
   - Depositar
   - Sacar
   - Ver Saldo
   - Render Juros (apenas Poupança)
   - Sair

### Exemplos de Interação:

**Teste 1: Conta Corrente com Limite**
```
- - BEM-VINDO AO EASYBANK - - 
Digite o nome: Maria Santos
Digite o CPF: 987.654.321-00
Digite o E-mail: maria@email.com

Cliente cadastrado:
Nome: Maria Santos
CPF: 987.654.321-00
E-mail: maria@email.com

ESCOLHA O TIPO DE CONTA PARA ABRIR
[1] - Corrente
[2] - Poupança
Digite 1 ou 2: 1

Digite o número da conta: 12345
Digite o limite da Conta Corrente: 1000

Conta Corrente criada com Sucesso!

Escolha a operação
1 - Depositar
2 - Sacar
3 - Saldo
0 - SAIR

Opção: 1
Digite o valor do depósito: 500
Depósito de R$500.00

Opção: 2
Digite o valor do saque: 1200
Saque de R$1200.00 realizado com sucesso!
(Saque permitido porque 1200 <= 500 + 1000)
```

**Teste 2: Conta Poupança com Rendimento**
```
- - BEM-VINDO AO EASYBANK - - 
Digite o nome: Pedro Costa
Digite o CPF: 111.222.333-44
Digite o E-mail: pedro@email.com

ESCOLHA O TIPO DE CONTA PARA ABRIR
[1] - Corrente
[2] - Poupança
Digite 1 ou 2: 2

Digite o número da conta: 67890
Conta Poupança criada com Sucesso!

Escolha a operação
1 - Depositar
2 - Sacar
3 - Render juros
4 - Saldo
0 - SAIR

Opção: 1
Digite o valor do depósito: 10000
Depósito de R$10000.00

Opção: 3
Digite a taxa de juros (ex: 0.10 = 10%): 0.05
Juros de R$500.00 aplicados!

Opção: 4
Saldo da conta 67890: R$10500.00

Opção: 0
(Programa encerrado)
```

---

## 🔑 Conceitos de POO Utilizados

### 1. **Encapsulamento** 🔒
```python
# Atributos protegidos com "_" (convenção Python)
self._saldo = 0
self._numero_conta = numero_conta
self._cliente = cliente

# Acesso seguro via properties
@property
def saldo(self):
    return self._saldo
```

### 2. **Herança** 👨‍👧‍👦
```python
# Subclasses herdam de ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, cliente, limite):
        super().__init__(numero_conta, cliente)  # Chama construtor da classe pai
        self._limite = limite
```

### 3. **Polimorfismo** 🔄
```python
# Método sacar é redefinido em cada subclasse
# ContaBancaria.sacar() → levanta exceção
# ContaCorrente.sacar() → permite até saldo + limite
# ContaPoupanca.sacar() → apenas até saldo disponível
```

### 4. **Validação e Tratamento de Erros** ⚠️
```python
# Validação em depositar
if valor > 0:
    self._saldo += valor
else:
    print("Valor Inválido!")

# Validação em sacar
if valor <= 0:
    print("Valor inválido!")
elif valor > self._saldo + self._limite:  # Exemplo ContaCorrente
    print("Saldo insuficiente!")
```

---

## 📁 Estrutura de Arquivos

```
Avaliacao-II/
├── cliente.py                 # Classe Cliente
├── conta_bancaria.py          # Classe base ContaBancaria
├── conta_corrente.py          # Subclasse ContaCorrente
├── conta_poupanca.py          # Subclasse ContaPoupanca
├── main.py                    # Programa principal com menu interativo
├── README.md                  # Este arquivo
└── __pycache__/              # Cache de bytecode Python
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior

### Executar o Programa
```bash
python main.py
```

### Estrutura de Entrada Esperada
```
1. Nome: João Silva
2. CPF: 123.456.789-00
3. Email: joao@email.com
4. Escolher tipo de conta (1 ou 2)
5. Número da conta
6. Se corrente: Valor do limite
7. Operações: Depositar, Sacar, Ver Saldo, Render Juros
```

---

## 📊 Diagrama UML (Texto)

```
┌─────────────────────────┐
│       Cliente           │
├─────────────────────────┤
│ - nome: str             │
│ - cpf: str              │
│ - email: str            │
├─────────────────────────┤
│ + exibir_dados()        │
└─────────────────────────┘
         ▲
         │
         │ usa
         │
┌─────────────────────────────────────────────────┐
│            ContaBancaria (Base)                 │
├─────────────────────────────────────────────────┤
│ # _numero_conta: str                            │
│ # _cliente: Cliente                             │
│ # _saldo: float                                 │
├─────────────────────────────────────────────────┤
│ + depositar(valor: float)                       │
│ + sacar(valor: float) [polimórfico]             │
│ + exibir_saldo()                                │
│ + @property saldo, cliente, numero_conta        │
└─────────────────────────────────────────────────┘
         ▲                           ▲
         │                           │
         │ herda                     │ herda
         │                           │
┌────────────────────┐    ┌──────────────────────┐
│  ContaCorrente     │    │   ContaPoupanca      │
├────────────────────┤    ├──────────────────────┤
│ # _limite: float   │    │ (sem atributos       │
├────────────────────┤    │  adicionais)         │
│ + sacar(valor)     │    ├──────────────────────┤
│   (com limite)     │    │ + sacar(valor)       │
│                    │    │   (sem limite)       │
│                    │    │ + render_juros(taxa) │
└────────────────────┘    └──────────────────────┘
```

---

## ✅ Checklist de Implementação

- ✅ Classe `Cliente` com atributos (nome, cpf, email)
- ✅ Classe `ContaBancaria` como base abstrata
- ✅ Atributos protegidos (`_numero_conta`, `_cliente`, `_saldo`)
- ✅ Métodos `depositar()` com validação
- ✅ Método `sacar()` polimórfico (redefinido nas subclasses)
- ✅ Método `exibir_saldo()` formatado
- ✅ Classe `ContaCorrente` com limite especial
- ✅ Classe `ContaPoupanca` com método `render_juros()`
- ✅ Validações de valores negativos
- ✅ Programa interativo com menu (`main.py`)
- ✅ Tratamento de erros e mensagens ao usuário

---

## 🎓 Conceitos de Aprendizado

Este projeto demonstra:

1. **Programação Orientada a Objetos (POO)**
   - Definição de classes
   - Atributos e métodos
   - Modificadores de acesso

2. **Herança**
   - Criação de classes especializadas
   - Reutilização de código
   - Método `super()`

3. **Polimorfismo**
   - Método `sacar()` redefinido em subclasses
   - Comportamento diferente baseado no tipo de conta

4. **Encapsulamento**
   - Proteção de dados sensíveis
   - Properties para acesso controlado
   - Validação de entrada

5. **Boas Práticas**
   - Validação de entrada
   - Mensagens de feedback ao usuário
   - Código limpo e bem organizado

---

## 💡 Possíveis Extensões Futuras

1. **Persistência em Banco de Dados**
   - Armazenar clientes e contas em SQL/NoSQL

2. **Autenticação**
   - Senha para acesso às contas

3. **Histórico de Transações**
   - Log de todas as operações

4. **Transferências**
   - Permitir transferências entre contas

5. **Taxa de Manutenção**
   - ContaCorrente com taxa mensal

6. **Diferentes Tipos de Juros**
   - Juros compostos na ContaPoupanca

7. **Interface Gráfica**
   - GUI com Tkinter ou PyQt

---

## 📝 Autor

Desenvolvedor Júnior - EasyBank

Data: Novembro de 2025

---

## 📞 Suporte

Para dúvidas sobre a implementação, consulte a documentação de cada classe ou execute o programa em modo interativo para testar as funcionalidades.

**Happy Banking! 🏦✨**
