# [Métodos de Classe](https://docs.python.org/pt-br/3/library/functions.html#classmethod)
Estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.

## Métodos de classe x métodos estáticos

* Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.

* Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo

## Quanto utilizar método de classe ou estático

* Geralmente usamos o método de classe para criar métodos de fábrica.
* Geralmente usamos métodos estáticos para criar funções utilitárias.


### Exemplo de codigo sem o usando método de classe

```Python
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Esse método retorna uma nova instância da classe com novos valores
    def criar_de_data_nascimento(self, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)

p = Pessoa('carlos', 35)
print(p.nome, p.idade)

# Dessa maneira é criado 2 intância de Pessoa no mesmo objeto
p2 = Pessoa().criar_de_data_nascimento(1988, 12, 20, 'jose')
print(p2.nome, p2.idade)

```

Quando há esse comportamento de fabrica, um método que retorna uma classe, a boa pratica é usarmos as classes de método

### Exemplo de codigo com o usando método de classe
* Para isso usamos o decorador @classmethod antes do [factory method](https://www.geeksforgeeks.org/factory-method-python-design-patterns/) (métodos que criam objetos),
também por convenção, não é usado self como referência da instância e sim cls
para a referência da classe.

* Na criação do objeto não é mais necessária a chamada da classe com os (), 
mas sim uma chamada como método (@classmethod)
    
  

```Python
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Esse método retorna uma nova instância da classe com novos valores
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
#
p = Pessoa('carlos', 35)
print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1988, 12, 20, 'jose')
print(p2.nome, p2.idade)

```

