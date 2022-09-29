#CRIANDO UMA TUPLA DE FORMA ITERATIVA

n = int(input())
tupla=()
for i in range(n):
    x = int(input())
    tupla = tupla +tuple([x])
    
print(tupla)    