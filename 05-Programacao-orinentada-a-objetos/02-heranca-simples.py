# essa vai ser a classe pai (super classe) que vai fornecer os atributos para
# todas as classes filho.

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Motor ligado')

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: \
{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):

    # sobreescrevendo a assinatura do construtor da classe pai com uma
    # nova assinatura
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado

        # incluindo os atributos da classe pai para serem usadas nessa classe
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(f'{"Sim" if self.carregado else "Não"} estou carregado')


moto = Motocicleta('branco', 'ABC-1234', 2)

carro = Carro('azul', 'AAA-1234', 4)

caminhao = Caminhao('preto', 'BBB-1234', 8, True)


print(caminhao)
print(carro)
print(moto)
