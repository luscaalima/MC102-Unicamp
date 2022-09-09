# Listas

# letras = ["A", "B", "C", "D", "E", "F","G"]
# i=0
# while i<len(letras):
#     print(letras[i])
#     i=i+1

# numeros = [3, 1, 7, 9, 4,15]
# maximo = 0
# i = 0
# while i < len(numeros):
#     if numeros[i] > maximo:
#         maximo = numeros[i]

#     i = i+1

# print(maximo)


# numeros = [-3, -1, -7, -9, -4, -15,0]
# maximo = numeros[-1]
# i = 1
# while i < len(numeros):
#     if numeros[i] > maximo:
#         maximo = numeros[i]

#     i = i+1

# print(maximo)


# FOR
# SINTAXE
# for <variavel> in <lista>:
#     <comando1>
#     <comando1>
#     <comando1>

# letras = ["A", "B", "C", "D", "E", "F","G"]

# for letra in letras :
#     print(letra)

# numeros = [3, 1, 7, 9, 4, 15, 0]
# maximo = 0
# for numero in numeros:
#     if numero > maximo:
#         maximo = numero

# print(maximo)

# print(list(range(2, 6)))
# for i in list(range(100)):
#     print(i)


n = int(input("Digite o tamanho da sua lista (n)"))
j = []
# criando uma lista com n elementos len(j) = n

# FOR
# for i in list(range(n)):
#     j.append(i+1)

# WHILE
i = 0
while (i < n):
    j.append(i+1)
    i = i+1
print(j)
print(len(j))
print(type(j))
