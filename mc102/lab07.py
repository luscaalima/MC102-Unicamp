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
print('defesa',defesa)
# Leitura das tropas de ataque
m= int(input())
ataque = []
for i in range(m):
    a= int(input())
    ataque.append(a)
print('ataque',ataque)
vitorias=0
empates=0
derrotas=0
# //*
index = 0
# Processamento da guerra
indexTwo=0
for i in defesa :
 for j in ataque:
    if j > defesa[indexTwo]:
     vitorias=vitorias+1
    elif j == defesa[indexTwo]:
     empates=empates+1        
    elif j<defesa[indexTwo]:
     derrotas=derrotas+1     
    indexTwo=indexTwo+1  
    
 if vitorias > derrotas:
     print(f'ganhou{indexTwo}')
     break
 elif vitorias < derrotas:
    pass
 elif vitorias==derrotas:
     pass
 vitorias=0
 empates=0
 derrotas=0
 indexTwo=0
 indexTwo=indexTwo+1
   

# print('vitorias ->',vitorias)
# print('empates ->',empates)
# print('derrotas ->',derrotas)    
        
            
# Saída de dados
# ...
# print('Derrota')
# ...
# print('Vitória posicionando as tropas a partir da posição', posicao)