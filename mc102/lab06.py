##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:Lucas Lima Pinheiro
# RA:263267
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split(' ')]
torreOrdenada = sorted(torre)

# print('torre',torre)
# print('torre Ordenada',torreOrdenada)
if torre == torreOrdenada:
  print('Torre estavel')
else:
    #faz um movimento 
    m = -1
    while m != 0:
        m = int(input())  
        movimento = torre[m:]
        movimento.sort(reverse=False)
        # print('movimento',movimento)
        # print('-->',torre[:m])
        torre = movimento+torre[:m]
        
    if torre == torreOrdenada:
     print('Torre estavel')
    else:
     print('Torre instavel') 
        
# Impressão da saída
