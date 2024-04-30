
class Conta:
    def __init__(self, n_agencia, _saldo=100):
        self.n_agencia = n_agencia

        # atributo privado para uso dento da classe
        self._saldo = _saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta(123, 100)
conta.depositar(100)

print(conta.n_agencia, conta.mostrar_saldo())
