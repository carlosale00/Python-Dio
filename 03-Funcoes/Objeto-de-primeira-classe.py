'''
Objetos de primeira classe
Em Python tudo é objeto, dessa forma funções também são
objetos o que as tornam objetos de primeira classe. Com isso
podemos atribuir funções a variáveis, passá-las como
parâmetro para funções, usá-las como valores em estruturas
de dados (listas, tuplas, dicionários, etc) e usar como valor de
retorno para uma função (closures).
'''


def somar(a: int | float, b: int | float):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'A soma de {a} e {b} é {resultado}')


exibir_resultado(1, 2, somar)
