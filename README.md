# preprocessAM

## Passo a passo da análise

## Base credit-data.csv

**Verificação de inconsistências**

Observou-se que as colunas income, age e loan estavam em formato de texto (string), contendo pontos adicionais que impediam a conversão direta para números.

**Correção de tipo de dados**

Essas colunas foram convertidas corretamente para o tipo numérico (float), permitindo operações matemáticas.

**Tratamento de valores ausentes (NA)**

Identificaram-se valores faltantes nessas colunas.

A estratégia escolhida foi substituir os valores ausentes pela média da respectiva coluna, mantendo a distribuição sem excluir registros.

**Resultado**

A base agora possui apenas valores válidos, numéricos e sem lacunas.

Foi salva como credit-data-tratado.csv.


## Base census.csv

**Identificação de valores inválidos**

Constatou-se que os valores ausentes eram representados pelo texto " ?", em vez de NA.

**Substituição de valores ausentes**

Todos os " ?" foram substituídos por NA, padronizando a representação de valores faltantes.

**Tratamento de valores ausentes por tipo de variável**

Para variáveis categóricas (ex.: workclass, occupation, native-country):

Os valores ausentes foram substituídos pela moda (valor mais frequente), garantindo consistência sem alterar a distribuição.

Para variáveis numéricas (ex.: idade, horas de trabalho):

Os valores ausentes foram substituídos pela mediana, escolhida por ser menos sensível a outliers do que a média.

**Resultado**

A base ficou livre de valores inválidos e padronizada para análises estatísticas.

Foi salva como census-tratado.csv.
