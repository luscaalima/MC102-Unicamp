
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
    print('matrizTransposta \n')     
    for i in range(len(matrizTransposta)):
        print(matrizTransposta[i])
#CRIANDO MATRIZ N x M 
l = int(input("Entre com o número de linhas: "))
c = int(input("Entre com o número de colunas: ")) 
matriz = []

for i in range(l):
     linhas = []
     for j in range(c):
         print(f'Digite o elemento : {i+1}.{j+1}')
         linha =int(input())
         linhas.append(linha)
     matriz.append(linhas)

        
print('matriz')
for i in range(len(matriz)) :
    print(matriz[i])      


transporMatriz(matriz)
