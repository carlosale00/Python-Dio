# Paradigmas de Programação

<p>Um paradigma de programaçaõ é um estilo.
<br>Não é uma linguagem <b>( Python C ,Java,etc)</b>, e sim uma forma  como você
soluciona os problemas atravéz do código.

<br><br>

# Paradigma Orientado a Objetos
<p>Estrutura o código abstraindo problemas em ojetos do mundo real, faciitando o entedimento do código e tornando-o
mais modular e extensível. Os dois conceiotos chave para aprender POO são: <b>Classes e Objetos</b>.


<br><br>

# CLasses e Objetos
Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretemente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas calsses.

<br><br>
# Herança

Em prgramação Herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai.

### beneficio
<li>Representa bem os relacionamentos do mundo real.
<li>Fornece reultilização de código, não precisamos escrever o código repetidamente. Além disso, permite adicionar recursos a uma classe sem modifica-lá.
<li>É de natureza transitiva, oque significa que , se a classe B herdar de classe A, todas as subclasses de B herdarão automaticamente de A

<br><br>
# Herança simple e multipla
### Simples: 
Quando a classe herda apenas de 1 classe pai.
## Uso/Exemplos

```Python
class A():
  pass

class B(A):
  pass
```
### Multipla :
Quando a classe herda de varias classes pai.

```Python
class A():
  pass

class B():
  pass

class C(A, B):
  pass

```