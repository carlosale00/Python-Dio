from abc import ABC, abstractmethod


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
    ...


class Historico:
    ...


class Transacao(ABC):
    ...


class Saque(Transacao):
    ...


class Deposito(Transacao):
    ...


if __name__ == '__main__':
    # c = Conta(1000, 1)
    # print(c.numero)
    # print(c.saldo)
    # print(c.agencia)
    # print(c.cliente)
    # print(c.historico)

    # c.depositar(100)
    # print(c.saldo)
    # c.sacar(50)
    # print(c.saldo)
    # c.sacar(50)
    # print(c.saldo)
    # c.sacar(0)
    # c.depositar(0)

    # c1 = Conta.nova_conta(1001, 1)
    # print(c1.numero)
    # print(c1.saldo)
    # print(c1.agencia)
    # print(c1.cliente)
    # print(c1.historico)

    # c1.depositar(100)
    # print(c1.saldo)
    # c1.sacar(50)
    # print(c1.saldo)
    # c1.sacar(50)
    # print(c1.saldo)
    # c1.sacar(1)
    # c1.sacar(0)
    # c1.depositar(0)

    # c2 = Conta.nova_conta(1002, 1)
    # print(c2.numero)
    # print(c2.saldo)
    # print(c2.agencia)
    # print(c2.cliente)
    # print(c2.historico)

    # c2.depositar(100)
    # print(c2.saldo)
    # c2.sacar(50)
    # print(c2.saldo)
    # c2.sacar(50)
    # print(c2.saldo)
    # c2.sacar(1)
    # c2.sacar(0)
    # c2.depositar(0)

    cc = ContaCorrente()
    ...
