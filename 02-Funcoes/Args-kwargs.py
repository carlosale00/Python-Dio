
'''
ARG E KWARGS
Podemos combinar parâmetros obrigatórios com args e
kwargs. Quando esses são definidos(*args e ** kwargs), o
método recebe os valores como tupla e dicionário
respectivamente.
'''


def exibir_poema(data, *args, **kwargs):

    texto = '\n'.join(args)
    meta_dados = '\n'.join(
        [f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])

    msg = f'{data}\n\n{texto}\n{meta_dados}'

    print(msg)


exibir_poema('17/04/2024',
             'Zen of python',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             'Beualtiful is better than ugly.',
             autor='Tim Peter',
             ano=1999)
