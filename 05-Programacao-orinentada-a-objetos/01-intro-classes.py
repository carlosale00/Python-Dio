
# criando uma classe
class Bicicleta:

    # metodo construtor da classe
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    # metodo da classe
    def buzinar(self):
        print('BiBi')

    def correr(self):
        print('a bicicleta esta correndo')

    def parar(self):
        print('a bicicleta esta parada')

    # método para retornar os atributos da classe dinamicamente
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: \
{', '.join([f'{chave} = {valor}'for chave, valor in self.__dict__.items()])}"

    # metodo desconstrutor
    def __del__(self):
        print('deletando instacia')


# instacia da classe
b1 = Bicicleta('azul', 'monark', 1990, 500)

print(b1)
