# Importando a classe ABC e a função
from abc import ABC, abstractmethod


class ControleRemoto(ABC):

    # usando o decorador para chamar a função
    @abstractmethod
    def ligar(self):
        ...

    @abstractmethod
    def desligar(self):
        ...

    @property
    @abstractmethod
    def marca(self, marca):
        return marca
        ...


class ControleTv(ControleRemoto):

    def ligar(self):
        print('Fui ligada por ', self.__class__.__name__)
        ...

    def desligar(self):
        print('Fui desligada por', self.__class__.__name__)
        ...

    def marca(self, marca):
        return marca


controle = ControleTv()

controle.desligar()
controle.ligar()

print(controle.marca('samsung'))
