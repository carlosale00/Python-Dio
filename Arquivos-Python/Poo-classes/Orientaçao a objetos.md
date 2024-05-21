# Paradigmas de Programação

<p>Um paradigma de programaçaõ é um estilo.
<br>Não é uma linguagem <b>( Python C ,Java,etc)</b>, e sim uma forma  como você
soluciona os problemas atravéz do código.

<br><br>

# Paradigma Orientado a Objetos
<p>Estrutura o código abstraindo problemas em ojetos do mundo real, faciitando o entedimento do código e tornando-o
mais modular e extensível. Os dois conceiotos chave para aprender POO são: <b>Classes e Objetos</b>.


<br><br>

# CLasses e Objetos
Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretemente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas calsses.

<br><br>
# Herança

Em prgramação Herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai.

### beneficio
<li>Representa bem os relacionamentos do mundo real.
<li>Fornece reultilização de código, não precisamos escrever o código repetidamente. Além disso, permite adicionar recursos a uma classe sem modifica-lá.
<li>É de natureza transitiva, oque significa que , se a classe B herdar de classe A, todas as subclasses de B herdarão automaticamente de A

<br><br>
# Herança simple e multipla
### Simples: 
Quando a classe herda apenas de 1 classe pai.
## Uso/Exemplos

```Python
class A():
  pass

class B(A):
  pass
```
### Multipla :
Quando a classe herda de varias classes pai.

```Python
class A():
  pass

class B():
  pass

class C(A, B):
  pass

```

Em OOP, herança é o mecanismo pelo qual estendemos a funcionalidade de uma classe. Por exemplo, suponha que a gente precise representar veículos de diferentes marcas e modelos em um programa. Uma abordagem é criar uma classe para representar cada veículo diferente. Porém, existem informações que são comuns a todos os veículos, como o tipo do veículo (motocicleta, carro, caminhão, etc.), chassi, marca, modelo, ano, e etc. Uma abordagem mais elegante é usar herança de modo a criar uma classe que armazena informações comuns a todos os tipos de veículos que precisamos representar e subsequentemente estender essa classe para representar veículos específicos. O exemplo abaixo mostra a classe Veiculo.

```Python

class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

```

Agora que sabemos como representar um veículo genérico, desejamos estender essa classe de modo a representar motocicletas. Suponha que, além das informações comuns a todos os veículos, motocicletas também contenham dados sobre a cilindrada da motocicleta em questão. Para representar uma motocicleta, podemos criar uma classe que herda o estado e comportamento da classe Veiculo e a estende de modo a adicionar informação sobre a cilidrada. O exemplo abaixo ilustra como fazer isso em Python.

```Python
class Motocicleta(Veiculo): 
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano) 
        self.cilindrada = cilindrada
```


Indica que a classe Motocicleta herda da classe Veiculo.<br>
Invoca o método init da super classe (ou classe base, Veiculo).

### [Classe super](https://docs.python.org/pt-br/3/library/functions.html#super):  
Retorna um objeto proxy que delega chamadas de método a uma classe pai ou irmão do type. Isso é útil para acessar métodos herdados que foram substituídos em uma classe.

### [Classe __mro __](https://docs.python.org/pt-br/3/library/stdtypes.html#class.__mro__): 
Este atributo é uma tupla de classes que são consideradas ao procurar por classes bases durante resolução de métodos.

Python tem duas funções embutidas que trabalham com herança:
### [isinstance(object, classinfo)](https://docs.python.org/pt-br/3/library/functions.html#isinstance):
 Retorna True se o argumento object é uma instância do argumento classinfo, ou de uma subclasse dele (direta, indireta ou virtual). Se object não é um objeto do tipo dado, a função sempre devolve False. Se classinfo é uma tupla de tipos de objetos (ou recursivamente, como outras tuplas) ou um Tipo União de vários tipos, retorna True se object é uma instância de qualquer um dos tipos. Se classinfo não é um tipo ou tupla de tipos ou outras tuplas, é levantada uma exceção TypeError. TypeError pode não ser levantada por um tipo inválido se uma verificação anterior for bem-sucedida

### [issubclass(class, classinfo)](https://docs.python.org/pt-br/3/library/functions.html#isinstance):
Retorna True se class for uma subclasse (direta, indireta ou virtual) de classinfo. Uma classe é considerada uma subclasse de si mesma. classinfo pode ser uma tupla de objetos de classe (ou recursivamente, outras tuplas) ou um Tipo União, caso em que retorna True se class for uma subclasse de qualquer entrada em classinfo. Em qualquer outro caso, é levantada uma exceção TypeError.