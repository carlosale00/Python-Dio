from abc import ABC
from datetime import datetime


class Cliente:
    ...


class PessoaFisica(Cliente):
    ...


class Conta:
    def __init__(self, numero, cliente) -> None:
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._agencia = '0001'
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        print("\n=== Nova conta criada com sucesso! ===")
        return cls(numero, cliente)

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):

        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        return True

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saque = valor > saldo

        if excedeu_saque:
            print("\n@@@ Operação falhou! Não possui mais saldo em conta. @@@")
            return False

        if valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saques

    # implementar a transaçao
    def sacar(self, valor):
        numero_saques = 1

        excedeu_limite = valor > self._saldo
        excedeu_saque = numero_saques > self._limite_saque

        if excedeu_limite:
            print('@@@ Operação Falhou! Você excedeu o seu limite da conta')
            return False

        if excedeu_saque:
            print('@@@ Operação Falhou! Você excedeu o seu limite de saques\
 diario')
            return False

        return super().sacar(valor)

    def __str__(self) -> str:
        return f'''
        Agencia:\t{self._agencia}
        Conta:\t\t{self._numero}
        Titular:\t
        Saldo:\t\tR${self._saldo:.2f}
        '''
    ...


class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    @transacoes.setter
    def add_transacoes(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': '',
                'data': datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            }
        )

        ...


class Transacao(ABC):

    ...


class Saque(Transacao):
    ...


class Deposito(Transacao):
    ...


if __name__ == '__main__':

    h = Historico()
    h.add_transacoes = 'saque'
    print(h.transacoes)
    ...
