###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome:Lucas Lima Pinheiro 
# RA: 263267
###################################################

# Leitura das tropas de defesa
n= int(input())
defesa = []
for i in range(n):
    d= int(input())
    defesa.append(d)
# Leitura das tropas de ataque
m= int(input())
ataque = []
for i in range(m):
    a= int(input())
    ataque.append(a)


posicao =None
index=0
indexTwo=0
vitorias=0
empates=0
derrotas=0

for i in defesa[:-len(ataque)+1]:
    indexTwo=indexTwo+1
    for j in ataque:
        if j > defesa[index]:
         vitorias=vitorias+1   
        elif j== defesa[index]:
          empates=empates+1      
        else :
            derrotas = derrotas+1    
        index=index+1
    
    if vitorias > derrotas:
        posicao = indexTwo
        break     
    else:
     index=indexTwo
     vitorias = 0
     derrotas = 0
     empates = 0
     continue  
 

if isinstance(posicao,int):
     print('Vitória posicionando as tropas a partir da posição', posicao)
elif posicao==None:
  print('Derrota')    