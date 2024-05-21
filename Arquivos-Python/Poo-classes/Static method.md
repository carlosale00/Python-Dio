# [@staticmethod](https://docs.python.org/pt-br/3/library/functions.html#staticmethod)

Transforma um método em método estático.

* Um método estático não recebe um primeiro argumento implícito e nao tem acesso nem a classe e a 
instância.

* Geralmente usamos métodos estáticos para criar funções utilitárias.

```Python
class C:
    @staticmethod
    def somar_valores(arg1, arg2, arg3):
      return arg1 + arg2 + arg3 ...

soma = C.somar_valores(1,2,3) #6
```
A forma @staticmethod é uma função de decorador

* Um método estático pode ser chamado na classe (tal como C.f()) ou em uma instância (tal como C().f()). Além disso, eles podem ser chamados como funções regulares (como f())