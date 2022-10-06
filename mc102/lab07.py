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
print(defesa)
# Leitura das tropas de ataque
m= int(input())
ataque = []
for i2 in range(m):
    a= int(input())
    ataque.append(a)
print(ataque)
vitorias=0
empates=0
derrotas=0
# Processamento da guerra
for i in ataque:
    for j in defesa:   
      # Ganhei uma batalha
      if j>i:
         vitorias =vitorias+1
      # Empatei uma batalha
      elif j == i:    
        empates= empates+1
     # Perdi uma batalha
      elif j<i:  
        derrotas=derrotas+1
    print('vitorias ->',vitorias)
    print('empates ->',empates)
    print('derrotas ->',derrotas)    
    if vitorias > derrotas:
        print('ganhou')
        break     
        
        
        
        
        
            
# Saída de dados
# ...
# print('Derrota')
# ...
# print('Vitória posicionando as tropas a partir da posição', posicao)