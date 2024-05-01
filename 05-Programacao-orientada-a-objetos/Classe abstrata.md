# [Classe abstrata](https://docs.python.org/pt-br/3/library/abc.html)

## interfaces:
 definem oque uma classe deve fazer ou não.

 O conceito de inteface é definido um contrato, onde são declarados os métodos
(o que deve ser feito) e suas respctivas assinaturas. Em python ultilizamos
calsses abstratas para criar contratos. Calsses abstratas não podem ser 
instanciadas.

 ## Crinado classes abstratas com o modulo ABC (Abstract Base Class)
  Por padrão , o python não fornece classes abstratas . O python vem com um 
módulo que fornece a base para definirmos as classes abtratas, e o nome é 
ABC.<br>
  O ABC funciona decorando métodos da classe base como abstratos e, em seguida, 
registrando
classes concretas como implementação de base abstrata. um método se torna abstrato
quando decorado com [@abstractmethod](https://docs.python.org/pt-br/3/library/abc.html#abc.abstractmethod).

```Python
# exemplo de classe abstrata

from abc import ABC, abstractmethod

# classe vai herdar a classe abstrata 
class ControleRemoto(ABC):

    # usando o decorador para chamar a função abtrata
    @abstractmethod
    def ligar(self):
        ...

    def desligar(self):
        ...
    
    @abste
    def marca(self):
      ...


class ControleTv(ControleRemoto):

    def ligar(self):
        print('Fui ligada por ', self.__class__.__name__)
        ...

    def desligar(self):
        print('Fui desligada por', self.__class__.__name__)
        ...


controle = ControleTv()

controle.desligar()
controle.ligar()

```

    * todos os cotratos firmados com a função abstractmethod são OBRIGATORIO a
    implementadas nas classes filhas, caso contrario levantara uma excessão.