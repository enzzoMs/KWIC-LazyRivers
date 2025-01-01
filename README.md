# KWIC - Key Word In Context (Lazy Rivers)

Este é um programa em Python que implementa o algoritmo [KWIC](https://en.wikipedia.org/wiki/Key_Word_in_Context) (Key Word In Context), utlizando o estilo de programação "Lazy Rivers", descrito no livro "[Exercises in Programming Style](https://www.amazon.com/Exercises-Programming-Style-Cristina-Videira/dp/1482227371)", escrito por Cristina Lopes.

## KWIC

O KWIC trata-se de uma técnica utilizada para indexar e buscar palavras-chave dentro de um texto, destacando o contexto em que essas palavras aparecem.

Exemplo:
```
O gato mia.
O cão late.
```     
O texto acima resulta em:
```  
cão late. O   from (O cão late.)
gato mia. O   from (O gato mia.)
late. O cão   from (O cão late.)
mia. O gato   from (O gato mia.)
```

## Estilo Lazy Rivers

No estilo Lazy Rivers:

* Os dados estão disponíveis em _streams_, em vez de serem processados como um todo.

* As funções são filtros/transformadores de um tipo de _streams_ de dados para outro.

* Os dados são processados a partir da fonte (upstream) conforme a necessidade do destino (downstream)

Este estilo foca no problema de processar dados que entram continuamente na aplicação e que podem não ter um fim definido. 

O estilo estabelece uma _stream_ de dados de uma fonte (upstream) para um destino (downstream), com unidades de processamento ao longo do caminho. 

Cada unidade de dados flui pelo caminho somente quando o destino precisa dele, evitando os problemas de ter que processar muitos dados ao mesmo tempo.

## Como Executar

Requisitos:
* [Python 3](https://www.python.org/)

### Programa Principal

Para executar o programa, basta rodar o arquivo `kwic.py` com o Python:


```
python ./KWIC/kwic.py <ARQUIVO>
```

Onde `<ARQUIVO>` é o caminho para o arquivo de texto que você deseja processar. O programa irá gerar os contextos das palavras-chave presentes no arquivo de texto fornecido.

### Executar os Testes

Os testes unitários do projeto estão implementados no arquivo `KWIC/test_kwic.py` e podem ser executados da seguinte forma:

```
python ./KWIC/test_kwic.py
```