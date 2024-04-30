# [PROPERTY](https://docs.python.org/pt-br/3/library/functions.html#property)

class property(fget=None, fset=None, fdel=None, doc=None)
Retorna um atributo de propriedade.

fget é uma função para obter o valor de um atributo. fset é uma função para definir um valor para um atributo. fdel é uma função para deletar um valor de um atributo. E doc cria um docstring para um atributo.

Um uso comum é para definir um atributo gerenciável x:

``` Python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
```
Se c é uma instância de C, c.x irá invocar o método getter, c.x = value irá invocar o método setter, e del c.x o método deleter.

Se fornecido, doc será a docstring do atributo definido por property. Caso contrário, a property copiará a docstring de fget (se ela existir). Isso torna possível criar facilmente propriedades apenas para leitura usando property() como um [decorador](https://docs.python.org/pt-br/3/glossary.html#term-decorator):

```Python
class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage
```

O decorador @property transforma o método voltage() em um “getter” para um atributo somente leitura com o mesmo nome, e define a docstring de voltage para “Get the current voltage.”

    decoradores de funçôes:
    @getter
    @setter
    @deleter


Com o property() do Python, você pode criar atributos gerenciados em suas 
classes. Você pode usar atributos gerenciados, também conhecidos como 
propriedades, quando precisar modificar sua implementação interna sem alterar a
API pública da classe.

    Um objeto property possui métodos getter, setter e deleter usáveis como 
    decoradores, que criam uma cópia da property com o assessor correspondente 
    a função definida para a função com decorador. Isso é explicado melhor com
    um exemplo:

``` Python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```
  
    O objeto property retornado também tem os atributos fget, fset, e fdel correspondendo aos argumentos do construtor.