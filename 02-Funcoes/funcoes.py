'''
CRIAÇAO DA FUNÇÃO:
Função é um bloco de código identificado por um nome e pode
receber uma lista de parâmetros, esses parâmetros podem ou
não ter valores padrões. Usar funções torna o código mais
legível e possibilita o reaproveitamento de código. Programar
baseado em funções, é o mesmo que dizer que estamos
programando de maneira estruturada.
'''


def exibir_mensagem(nome):
    print(f'ola {nome}')


exibir_mensagem('Carlos')


'''
RETORNO:
Para retornar um valor, utilizamos a palavra reservada return .
Toda função Python retorna None por padrão. Diferente de
outras linguagens de programação, em Python uma função
pode retornar mais de um valor.
Retornando valores
[8]
'''


def somar_valores(x, y):
    return x + y


print(somar_valores(1, 2))
'''

ARGUMENTOS NOMEADOS:
Funções também podem ser chamadas usando argumentos
nomeados da forma chave = valor.
Argumentos nomeados
[10]

'''

# paramêtro explicito


def salvar_carro(marca, modelo, ano=1990):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}')


# normal
salvar_carro('Fiat', 'Palio')
# argumentos nomeados
salvar_carro(marca='Fiat', modelo='Palio', ano=2010)
