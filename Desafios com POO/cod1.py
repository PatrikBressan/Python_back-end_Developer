from abc import ABC, classmethod, abstractmethod
from datetime import datetime


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\nOperação falhou! Você não tem saldo suficiente.')
        elif valor > 0:
            self._saldo -= valor
            print('\nSaque realizado com sucesso!')
            return True
        else:
            print('\nOperação falhou! O valor informado é inválido')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\nDepósito realizado com sucesso!')
        else:
            print('\nOperação inválida: não é permitido depositar valor nulo e/ou negativo')
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    # Sobreescrita do método sacar, para fazermos algumas validações
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('\nOperação inválida: o valor do saque excede o limite.')
        elif excedeu_saques:
            print('\nOperação inválida: número máximo de saques excedido')
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            Conta corrente:\t{self.numero}
            Titular:\t{self.cliente.nome}
        '''

class Historico:
    def __init__(self):
        self._transacaoes = []
    
    @property
    def transacoes(self):
        return self._transacaoes
    
    def adicionar_transacao(self, transacao):
        self._transacaoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento