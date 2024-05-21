# ENCAPSULAMENTO:

## PROTEÇÃO DE ACESSO:
O encapsulamento é um dos conceitos fundamentais em
programação orientada a objetos. Ele descreve a ideia de
agrupar dados e os métodos que manipulam esses dados em
uma unidade. Isso impõe restrições ao acesso direto a
variáveis e métodos e pode evitar a modificação acidental de
dados. Para evitar alterações acidentais, a variável de um
objeto só pode ser alterada pelo método desse objeto.

## MODIFICADORES DE ACESSO:
Em linguagens como Java e C++, existem palavras reservadas
para definir o nível de acesso aos atributos e métodos da
classe. Em Python não temos palavras reservadas, porém
usamos convenções no nome do recurso, para definir se a
variável é pública ou privada.

## DEFINIÇÃO:
* Público: Pode ser acessado de fora da classe.
* Privado: Só pode ser acessado pela classe.

## PUBLICO / PRIVADO:
Todos os recursos são públicos, a menos que o nome inicie
com <b>underline</b> ( _atributo). Ou seja, o interpretador Python não irá
garantir a proteção do recurso, mas por ser uma convenção
amplamente adotada na comunidade, quando encontramos
uma variável e/ou método com nome iniciado por underline,
sabemos que não deveríamos manipular o seu valor
diretamente, ou invocar o método fora do escopo da classe.

### Exemplo de codigo encapsulado 

    Podemos acessar o atributo _saldo diretamente ,mais não é uma boa pratica pois
    ele é um atributo é privado ,para isso criamos um método que recebe o valor
    desse atributo e nele fazer algumas validações necessaria e ai mostraremos 
    o saldo.

```Python
class Conta:
    def __init__(self, n_agencia, _saldo=100):
        self.n_agencia = n_agencia
        # atributo privado para uso dento da classe
        self._saldo = _saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta(123, 100)
conta.depositar(100)

# forma errada pois esse método é privado
print(conta._saldo)

#forma correta
print( conta.mostrar_saldo())

```