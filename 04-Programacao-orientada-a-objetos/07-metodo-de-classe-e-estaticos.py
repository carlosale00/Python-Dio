# classmethod
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # factory function
    @classmethod  # metodo de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    # método estatico
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa('carlos', 35)
print(p.nome, p.idade)

# criando uma novo objeto
p2 = Pessoa.criar_de_data_nascimento(1988, 12, 20, 'jose')
print(p2.nome, p2.idade)

# hamando o metodo statico da classe
print(Pessoa.e_maior_idade(p2.idade))
