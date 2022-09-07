# REPETIÇÃO COM WHILE
#  IMPRIMINDO TODOS OS NÚMEROS INTEIROS DE 1 ATÉ 100
# i = 0
# while (i < 100):
#     i = i+1
#     print(i)

#  IMPRIMINDO TODOS OS NÚMEROS INTEIROS DE 1 ATÉ N
# n = int(input("Digite um numero..."))
# i = 1
# while (i <= n):
#     print(i)
#     i = i + 1
# print("Fim do programa...")

# CONTAGEM REGRESSIVA
# n = int(input("Digite um numero..."))
# i = 1
# while (n >= 0):
#     print(n)
#     n = n - 1

# print("BOOM !!")

# dividendo = int(input("Dividendo..."))
# divisor = int(input("Divisor..."))

# quociente = 0
# while (dividendo >= divisor):
#     dividendo = dividendo-divisor
#     quociente = quociente+1

# print("Quociente", quociente)
# print("Resto", dividendo)
# // ??
base = float(input("Base"))
expoente = int(input("Expoente"))
result = base
i = 1
while (i < expoente):
    result = result*base
    i = i+1

print(result)
