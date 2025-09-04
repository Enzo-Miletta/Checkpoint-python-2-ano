import unicodedata
import heapq

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def contar_letras(frase):
    frase = remover_acentos(frase.lower())
    tabela = {}

    for letra in frase:
        if letra.isalpha():
            tabela[letra] = tabela.get(letra, 0) + 1

    # Cria uma heap com tuplas (letra, contagem)
    heap = []
    for letra, contagem in tabela.items():
        heapq.heappush(heap, (letra, contagem))

    # Imprime as letras em ordem alfabética usando a heap
    while heap:
        letra, contagem = heapq.heappop(heap)
        print(f"{letra}: {contagem}", end="  ")

# Exemplo de uso
entrada = input("Digite uma frase: ")
contar_letras(entrada)