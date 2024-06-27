def piramide_alfabetica(N, maiusculas):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if maiusculas else 'abcdefghijklmnopqrstuvwxyz'

    for i in range(N):
        linha = '.' * (N - i - 1)  # preenche com pontos
        linha += alfabeto[:i + 1]  # adiciona letras do alfabeto
        linha += '.' * (N - i - 1)  # preenche com pontos
        print(linha)

# Exemplo de uso:
N = int(input("Digite o número de linhas da pirâmide: "))
P = input("Digite 'maiusculas' ou 'minusculas' para escolher o tipo de letras: ")

if P.lower() == 'maiusculas':
    piramide_alfabetica(N, True)
elif P.lower() == 'minusculas':
    piramide_alfabetica(N, False)
else:
    print("Entrada inválida. Por favor, escolha 'maiusculas' ou 'minusculas'.")