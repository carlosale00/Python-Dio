"""
Properties

Com o property() do Python, você pode criar atributos
gerenciados em suas classes. Você pode usar atributos
gerenciados, também conhecidos como propriedades, quando
precisar modificar sua implementação interna sem alterar a
API pública da classe.

"""


class Foo():
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, valor):
        _x = self.x or 0
        _valor = valor or 0
        self._x = _x + _valor

    @x.deleter
    def x(self):
        self._x -= 1


foo = Foo(80)
print(foo.x)

foo.x = 100
print(foo.x)

del foo.x
print(foo.x)
