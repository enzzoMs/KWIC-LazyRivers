"""
KWIC - Keyword in Context

Este projeto implementa o algoritmo Keyword in Context (KWIC). Este algoritmo recebe uma lista 
de títulos ou frases e gera uma lista alfabetizada de todas as palavras-chave nesses títulos, 
juntamente com seu contexto circundante.

A implementação do algoritmo segue o estilo 'Lazy Rivers', descrito pela Profa. Crista Lopes
em seu livro 'Exercises in Programming Style'.

Uso:
    python kwic.py <caminho_do_arquivo>

"""

import os
import sys

STOP_WORDS = [
    "a", "o", "e", "as", "os", "um", "uma", "uns", "umas", "é", "são", "de", "do", "da", "dos", "das", 
    "em", "no", "na", "nos", "nas", "por", "para", "com", "se", "que", "ou", "mas", "como", "tal"
]

def read_lines_from_file(file_path):
    """
    Lê as linhas de um arquivo e as retorna uma a uma.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

def get_words_in_line(line):
    """
    Divide uma linha em palavras e as retorna uma a uma.
    """
    for word in line.split():
        yield word

def find_keywords_in_line(line):
    """
    Identifica palavras-chave em uma linha, desconsiderando 
    palavras irrelevantes. Para cada palvra-chave, retorna 
    uma tupla contendo a palavra e o seu contexto original.
    """
    for word in get_words_in_line(line):
        if word.lower() not in STOP_WORDS:
            yield (word, line)

def highlight_keyword_in_line(keyword, line):
    """
    Destaca a palavra-chave em uma linha, movendo-a 
    para o início.
    """
    words = line.split()
    keyword_index = words.index(keyword)
    return " ".join(
        words[keyword_index:] + words[:keyword_index]
    )

def generate_kwic(file_path):
    """
    Identifica palavras-chave em um arquivo, desconsiderando
    palavras irrelevantes e gera uma lista delas com seus 
    respectivos contextos. Retorna uma tupla contendo uma linha 
    com a palavra-chave destacada e a linha original (sem destaque).
    """
    for line in read_lines_from_file(file_path):
        for keyword, keyword_line in find_keywords_in_line(line):
            keyword_in_context = highlight_keyword_in_line(keyword, keyword_line)
            yield (keyword_in_context, keyword_line)
            
def print_kwic(file_path):
    """
    Imprime os resultados do algoritmo KWIC. Cada palavra-chave
    é exibida em ordem alfabética com seu contexto original.
    """
    kwic_list = []
    for kwic in generate_kwic(file_path):
        kwic_list.append(kwic)
        
    max_line_length = max([len(kwic) for kwic, _ in kwic_list])

    for kwic, original_line in sorted(kwic_list):
        print(f"{kwic.ljust(max_line_length)}    (from \"{original_line}\")")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERRO: Especifique um arquivo de entrada.")
        print("Ex: python ./kwic.py <caminho_do_arquivo>\n")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"Error: O arquivo '{file_path}' não existe.")
        sys.exit(1)

    print_kwic(file_path)