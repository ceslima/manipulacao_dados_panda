# manipulacao_dados_panda
funções para ver dados de novo dataframe

Inspeção de um DataFrame
Quando você recebe um novo DataFrame para trabalhar, a primeira coisa que precisa fazer é explorá-lo e ver o que ele contém. Há vários métodos e atributos úteis para isso.

.head() retorna as primeiras linhas (a parte superior do DataFrame).
.info() mostra informações sobre cada uma das colunas, como o tipo de dados e o número de valores ausentes.
.shape retorna o número de linhas e colunas do DataFrame.
.describe() calcula algumas estatísticas de resumo de cada coluna.
homelessness é um DataFrame que contém estimativas da falta de moradia em cada estado dos EUA em 2018. A coluna individual é o número de indivíduos sem-teto que não fazem parte de uma família com filhos. A coluna family_members é o número de indivíduos sem-teto que fazem parte de uma família com filhos. A coluna state_pop é a população total do estado.

pandas foi importado para você.
