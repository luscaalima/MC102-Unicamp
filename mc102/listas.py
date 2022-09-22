# n = int(input("Quantos números serão lidos? "))
# lista = []
# for i in range(n):
#     lista.append(int(input()))
#     x = int(input("Qual o número a procurar? "))
#     if x in lista:
#      print(x, "pertence à lista")
#     else:
#      print(x, "não pertence à lista")
     
## TUPLAS

# n = int(input("Quantos números serão lidos? "))
# tupla = ()

# for i in range(n): 
#     x  = int(input("Digite um numero"))
#     tupla = tupla + tuple([x])
    
# print(type(tupla))       
# print(tupla)    
    
    
# Dada uma lista L de n valores inteiros, escreva um programa que
# remova todos os números pares da lista.
# n = int(input("N"))
# l = list(range(1,n+1))
# print("lista",l)   
# print("tamanho lista",len(l))   

# for i in l :
#    if (i%2) == 0:
#        l.remove(i)


# print("lista com somente números impares",l)   
# print("tamanho lista" ,len(l)) 

##
# l = int(input("Entre com o número de linhas: ")) # l = 3
# c = int(input("Entre com o número de colunas: ")) # c = 4
# matriz = []
# for i in range(l):
#     linha = []
#     for j in range(c):
#         linha.append(0)
#         matriz.append(linha)

# print(matriz[0])
# [
#     [0, 0, 0, 0], 
#     [0, 0, 0, 0], 
#     [0, 0, 0, 0]
# ]
# Acessando Elementos de uma Matriz
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #3X3
# print(matriz)
# pegar o elemento 5
# print(matriz[2][1])


# Exercício 2 - Dimensões de uma Matriz
def dimensões(M):
 linhas = len(M)
 colunas = len(M[0])
 for i in range(1, linhas):
    if len(M[i]) != colunas:
     return ()
 return (linhas, colunas)

# Exercício 3 - Imprimindo uma Matriz
def imprime_matriz(M):
 (linhas, colunas) = dimensões(M)
 for i in range(linhas):
    for j in range(colunas):
     print(M[i][j], end = " ")
 print()


def transporMatriz(matriz):
    linhasOld =len(matriz)
    colunasOld = len(matriz[0])
    # TRANSFORMA UMA MATRIZ MxN EM UMA MATRIZ NxM
    linhasNew= []
    matrizTransposta = []
    for j in range(colunasOld):
        linhasNew= []
        for i in range(linhasOld):
           linhasNew.append(matriz[i][j]) 
        matrizTransposta.append(linhasNew) 
    print('matrizTransposta')     
    for i in range(len(matrizTransposta)):
        print(matrizTransposta[i])
#CRIANDO MATRIZ N x M 
l = int(input("Entre com o número de linhas: ")) # l = 3
c = int(input("Entre com o número de colunas: ")) # c = 4
matriz = []

for i in range(l):
     linhas = []
     for j in range(c):
         print(f'Digite o elemento : {i+1}.{j+1}')
         linha = int(input())
         linhas.append(linha)
     matriz.append(linhas)

        
print('matriz')
for i in range(len(matriz)) :
    print(matriz[i])      


transporMatriz(matriz)
