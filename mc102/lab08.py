###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Lucas Lima Pinheiro
# RA: 263267
###################################################

# Leitura da palavra
palavra = input()
arrayPalavra = []
for letter in palavra:
  arrayPalavra.append(letter)
# print(arrayPalavra)

chutes =[]
#Monta array chutes
for i in range(6):
  chute = input()
  chutes.append(chute)
# print('chutes',chutes)
arrayShow=[]
index=0
world=''
for chute in chutes:
#  print('chute',chute)
 for letter in palavra :
   if index <= len(palavra):
    if letter in chute :
      # print('index',index)
      # print('chute',chute[index])
      if letter == chute[index]:
        world += letter.upper()
      else:
        world += letter
    else:
     world +='_'
   index=index+1  
 print('world',world)     
 arrayShow.append(world) 
    
print(arrayShow)
     
# Leitura dos palpites e impressão do resultado para cada palpite 
   
# Impressão da linha final
# ...
# if flag 
# print("Resposta correta")
# # ...
# print("Palavra correta:", palavra)
