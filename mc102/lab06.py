##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:Lucas Lima Pinheiro
# RA:263267
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split(" ")]
torreOrdenada = sorted(torre)

while True:
    m = int(input())
    if m == 0:
        break
    else:
        if m >= len(torre):
            torre = list(reversed(torre))
        else:
            movimento = torre[:m]
            movimento = list(reversed(movimento))
            torre = movimento + torre[m:]

if torre == torreOrdenada:
    print("Torre estavel")
else:
    print("Torre instavel")

# Impressão da saída
