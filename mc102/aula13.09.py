#LAÇOS ALINHADOS
#TABUADA DOS NÚMEROS DE 1 A 10

# for i in range(1,11):
#     print("TABUADA DO",i,":")
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)

# n = int(input("Linhas"))
# m = int(input("Colunas"))

# for i in range(n):
#     for j in range(m):
#         print("#",end="")
# print()   

# for i in range(4):
#     print("#"*3)   


#IMPRIMINDO UM TRIÂNGULO RETÂNGULO ISÓSCELES COM CATETOS DE TAMANHO DADO

# n = int(input("CATETOS"))
# c = input("CARACTERE A SER USADO")
# for i in range(1,n+1):
#     for j in range(i):
#         print(c,end="")
# print()       

#IMPRIMINDO TODAS OS HORARIOS DE UM DIA NO FORMATO HH:MM:ss
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#         # print(h,m,sep=":")
#          print('{:02d}:{:02d}:{:02d}'.format(h,m,s))


# IMPRIMINDO TODOS DIVISORES DE UM NUMERO INTEIRO POSITIVO

# n= int(input("N:"))
# for divisor  in range(1,n+1):
#     if n % divisor == 0:
#         print("Divisor",divisor)

# IMPRIMINDO A FATORAÇÃO DE  N EM NÚMEROS PRIMOS

n= int(input("N:"))
divisor=2
while n != 1:
    if n % divisor == 0:
        print(divisor)
        n=n/divisor
    else:
        divisor=divisor+1    