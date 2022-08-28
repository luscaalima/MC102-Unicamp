# nome = input("Qual o seu nome ?")

# Estrutura de decisão

# if nome == "Lucas":
#     print("O nome bateu ")
#     idade = input("Qual sua idade")
#     if idade == "21":
#         print("Idade bateu")
#     else:
#         print("O nome bateu mas a idade não")
# else:
#     print("O nome não bateu ")


nomes = ["Lucas", "João"]
print(nomes)
nomeTemporario = input("Digite seu nome")
nomes.append(nomeTemporario)
print(nomes)

for nome in nomes:
    print(nome)