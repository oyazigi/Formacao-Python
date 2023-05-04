from abc import ABC, abstractmethod
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta._historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        if conta.registrar(self._valor):
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._historico = []

    def adicionar_transacao(self,transacao):
        self._historico.append(f'{transacao.__class__.__name__} de {transacao._valor} efetuada')

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, agencia, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self):
       return float(self._saldo)

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, "4500", numero)

    def sacar(self, valor):
        if self._saldo > valor:
            self._saldo += valor
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            return False

class ContaCorrente(Conta):
    def __init__(self,  numero, cliente, limite=500, limite_saques=3):
        self._limite = limite
        self._limite_saques = limite_saques
        super().__init__(numero, cliente)

c1 = PessoaFisica('45048958740','Victor','03/03/2001', 'Rua sete mares')
b1 = Cliente('rua da represa')
d1 = Historico()
a1 = Conta(500, '45896587450', '0001')
print(a1.saldo())
x1 = Conta.nova_conta(b1,'4500')
a1.depositar(1000)
print(a1.saldo())
b1.realizar_transacao(a1,Deposito(200))