'''
DESAFIO

Fomos contratados por um grande banco para desenvolver o seu novo sistema.
* Devemos implementar 3 operações : Deposito, Saque e Extrato.
* Deve ser possível depositos de valores positivos
* A V1 trabalha apenas com 1 usuário.
* Todas os depósitos devem ser armazenados em uma variável e exibidas
na operação extrato.
* Sistema deve permitir apenas 3 saque diários com limíte de 500 Reais
* Caso usuário nnão tenha saldo, exibir uma mensagem que não será
possivel sacar
* Todos os saques serão armazenados em uma variável e exibidas na
operação extrato.
'''

menu = '''Sistema Bancario TAL\n
0- para sair
1 -Saque
2- Deposito
3- Extrato '''

saque = 0
deposito = 0
extrato = 0

LIMITE_SAQUES = 3
saques = 0

while True:

    try:
        print(menu)
        opçao = int(input('Escolha a operaçao desejada: '))

        if opçao == 0:
            print('\nSaindo do sistema')
            break

        elif opçao == 1:
            print('\nSAQUE')
            saques += 1
            if saques > LIMITE_SAQUES:
                print('Limite de saques diarios atingidos')
                break

            if extrato == 0:
                print('Sem saldo na conta para sacar\n')
                continue
            else:
                saque = float(input('Valor de saque desejado: '))

                if saque > extrato:
                    print(
                        f'Saque não permitido tente um valor menor ou igual a R${extrato}')
                    continue
                else:
                    print(f'Você sacou R${saque} e seu saldo é {extrato}')
                    continue

        elif opçao == 2:
            print('DEPOSITO')
            deposito += float(input('Digite o valor do seu deposito: '))

        elif opçao == 3:
            print('EXTRATO')
            print(f'Saldo da sua conta é R${extrato}')
        else:
            print('Opção invalida')

    except:
        print('Opção invalida use apenas 0, 1, 2 ou 3')
