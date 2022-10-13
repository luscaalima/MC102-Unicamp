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
  if chutes[-1]== palavra:
    break
# print('chutes',chutes)
arrayShow=[]

 #cHUTE COM A PALAVRA
flag = None
for chute in chutes:
 if chute == palavra:
   arrayShow.append(chute.upper())
   flag=True
   break
 else :
  index=0
  world=''
  if len(chute)==len(palavra):
    for letter in  chute :
      if letter in palavra:
        if letter == palavra[index]:
          world += letter.upper()
        else:
          world += letter.lower()  
      else:
        world += '_'
      index = index + 1  
  elif len(chute)>len(palavra): 
    print('-->',chute[:len(palavra)])
    for letter in  chute[:len(palavra)] :
      if letter in chute:
        if letter == chute[index]:
          world += letter.upper()
        else:
          world += letter.lower()  
      else:
        world += '_'
      index = index + 1  
#len(chute)<len(palavra)
  else:
     for letter in  chute :
      # print(palavra[index],'==',letter)
      # print('index',index)
      # print(palavra[index])
      if letter in palavra:
        if letter == palavra[index]:
          world += letter.upper()
        else:
          print('letter',letter)
          world += letter.lower()  
      else:
        world += '_'
      index = index + 1  
      
 arrayShow.append(world)

#  print('chute',chute)
 
 
#  print('world',world)     
#  arrayShow.append(world) 
    
# print(arrayShow)
     
# Leitura dos palpites e impressão do resultado para cada palpite 
   
# Impressão da linha final
# ...
for i in arrayShow:
    print(i)
    
if flag :
 
  print("Resposta correta")
# ...
else:
 print("Palavra correta:", palavra)
