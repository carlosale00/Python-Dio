'''
Heranças são recursos potentes na linguagem python, mais podem ocasionar do 
seu código ficar extrememente complexo , USAR COM MODERAÇAO'''


class Animal:
    def __init__(self, n_patas) -> None:
        self.n_patas = n_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: \
{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


'''
Esta sendo usada o argumento KWargs para receber os atributos da classe pai pois
temos a classe Ornintorrinco que tem uma herança multipla com a classe Animal e 
Ave e na instância ela da erro pois aguarda a passagem os paramêtros delas.  

usando o KWargs ele vai receber n atributos sem gerar erro , mais a instância 
dos objetos devem ser passados nomeados, para nao causar erro 
'''


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornintorrinco(Ave, Mamifero):
    pass


gato = Gato(cor_pelo='Branco', n_patas=4)
print(gato)

ornintorrinco = Ornintorrinco(n_patas=2, cor_pelo='preto', cor_bico='verde')
print(ornintorrinco)
