Commits semânticos
São uma convenção simples para ser utilizada nas mensagens de commit. Esses commits auxiliarão você e sua equipe a entenderem de forma facilitada quais alterações foram realizadas no trecho de código que foi commitado.

Essa identificação ocorre por meio de uma palavra e emoji que identifica se aquele commit realizado se trata de uma alteração de código, atualização de pacotes, documentação, alteração visual, teste entre outros.

Exemplo:
git commit -m ":tada:commit inicial"
Utilizar esse padrão é bem simples, basta adicionar um título e um emoji no início da mensagem de commit representado sobre o commit. Em nosso caso foi o :tada: que representa o commit inicial.

É recomendável que na primeira linha deva ter no máximo 4 palavras e para descrever com detalhes, usar a descrição commit.

:FEAT:
Indicam que se trecho de código está incluindo um novo recurso.

:FIX:
Indicam que seu trecho de código commitado está solucionando um problema (bug fix)

:DOCS:
Indica que houve mudanças na documentação, como por exemplo no README do seu repositório.

:TEST:
São utilizados quando são realizadas alteração em testes, seja criando, alterando ou excluindo testes unitários.

:BUILD:
Commits do tipo build são utilizados quando são realizadas alterações em arquivos de build e dependências.

:RERF:
Servem para indicar quaisquer alterações de código que estejam relacionadas a performance.

:STYLE
Indica que houve alterações relacionadas a formatações de código, semicolons, trailing spaces, lint...

:CHORE:
Indicam atualizações de tarefas de build, configurações, pacotes... Como por exemplo adicionar um pacote no gitignore.

:CI:
Indicam mudanças relacionadas a integração contínua (continuos integration).

:REFACTOR:
Refere-se a mudanças devido a refatorações que não alterem sua funcionalidade, como por exemplo uma alteração no formatado como é processada de