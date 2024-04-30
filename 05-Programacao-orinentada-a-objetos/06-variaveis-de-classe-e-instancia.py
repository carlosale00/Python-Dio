'''
Atributos de classe:
Todos os objetos nascem com o mesmo número de atributos
de classe e de instância. Atributos de instância são diferentes
para cada objeto (cada objeto tem uma cópia), já os atributos
de classe são compartilhados entre os objetos.

'''


class Estudande:

    # Variavel de classe
    escola = 'DIO'

    def __init__(self, nome, numero) -> None:
        self.nome = nome
        self.numero = numero

    def __str__(self) -> str:
        return f'{self.nome} ({self.numero} - {self.escola} )'


carlos = Estudande('Carlos', 1)
marcos = Estudande('marcos', 2)
print(carlos)
print(marcos)


# Alterando o valor da variável na classe que afetara todas as instâncias
Estudande.escola = 'nada'
print(carlos)
print(marcos)

# Alterando o valor da variável de instância que vai afetar apenas essa
# instância.
carlos.escola = 'sesi'
print(carlos)
