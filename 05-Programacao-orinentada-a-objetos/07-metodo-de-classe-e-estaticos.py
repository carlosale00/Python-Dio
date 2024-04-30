# classmethod

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # factory function
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)


p = Pessoa('carlos', 35)
print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(1988, 12, 20, 'jose')
print(p2.nome, p2.idade)
