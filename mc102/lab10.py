#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome:Lucas Lima Pinheiro
# RA:263267
#####################################################

# Leitura da matriz

n = int(input())
matriz = [input().split() for _ in range(n)]
# print('n',matriz)
# for i in range(len(matriz)) :
#     print(matriz[i])   
    
time = input()
m= int(input())
tesourosAzul = 0
tesourosVermelho = 0

for j in range(m):
    caminho = input()
    linha = 0 
    coluna = 0
    for cordenada in caminho :
     if cordenada =='N':
      linha = linha-1
      if matriz[linha][coluna] =='*':
         if time =='azul':
             tesourosAzul = tesourosAzul+1       
         else:
              tesourosVermelho = tesourosVermelho+1  
         matriz[linha][coluna]='.'
     elif cordenada =='S':
      linha = linha+1  
      if matriz[linha][coluna] =='*': 
        if time =='azul':
         tesourosAzul = tesourosAzul+1       
        else:
         tesourosVermelho = tesourosVermelho+1  
      matriz[linha][coluna]='.'
     elif cordenada =='O':
      coluna = coluna-1  
      if matriz[linha][coluna] =='*':
         if time =='azul':
             tesourosAzul = tesourosAzul+1       
         else:
              tesourosVermelho = tesourosVermelho+1  
         matriz[linha][coluna]='.'
     else :
      coluna = coluna+1  
      if matriz[linha][coluna] =='*':
         if time =='azul':
             tesourosAzul = tesourosAzul+1       
         else:
              tesourosVermelho = tesourosVermelho+1  
         matriz[linha][coluna]='.'

    if time == 'azul': 
     time = 'vermelho'
    else:
     time='azul' 




print ('Tesouros encontrados pelo time azul: '+str(tesourosAzul)+'\nTesouros encontrados pelo time vermelho: '+str(tesourosVermelho))
if tesourosVermelho>tesourosAzul:
    print('Vitoria do time vermelho')
elif tesourosVermelho==tesourosAzul:   
    print('Empate') 
else:
    print('Vitoria do time azul')
