##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome:Lucas Lima Pinheiro
# RA:263267
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split(' ')]
torreOrdenada = sorted(torre)
# print('torre ->',torre)

# if torre == torreOrdenada:
#   print('Torre estavel')
# else:
    #faz um movimento 
while True:
#   print(m)
  m = int(input())  
  if m== 0:
      break
  
  if m >= len(torre) : 
    torre = list(reversed(torre))
  
  
  
  
  
  
  movimento = torre[:-m] # OK
  # print('movimento',movimento)
  movimento = list(reversed(movimento))
  # print('movimento reversed',movimento) #OK
  # print('-->',torre[:m])
  torre = movimento+torre[:m]

# print('torre',torre)
# print('torre Ordenada',torreOrdenada)       
if torre == torreOrdenada:
 print('Torre estavel')
else:
 print('Torre instavel') 
        
# Impressão da saída
