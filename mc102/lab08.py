###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Lucas Lima Pinheiro
# RA: 263267
###################################################

# Leitura da palavra
palavra = input()
chutes =[]
#Monta array chutes
for i in range(6):
  chute = input()
  chutes.append(chute)
print('chutes',chutes)
arrayShow=[]

for chute in chutes:
    
    if chute == palavra:
        arrayShow.append(palavra)
    else : 
        palavra=palavra.split()
        if len(palavra)>len(chute):
            
            chute= chute.split()
            index1=0
            string=''
            for letra in chute:
                
                if palavra[index1]==chute[index1]:
                  string+=palavra[index1]
                else:
                
                
        else:
        
  
  

# Leitura dos palpites e impressão do resultado para cada palpite 
   
# Impressão da linha final
# ...
if flag 
print("Resposta correta")
# ...
print("Palavra correta:", palavra)
