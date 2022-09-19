###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome:Lucas Lima Pinheiro
# RA: 263267
###################################################

# leitura da sequência de compras e vendas
operacao = int(input())
total_estoque = 0
quantidade_vendas = 0
msg_erro= 0
errosArray = []
while operacao != 0:

    if operacao > 0:
        total_estoque = operacao + total_estoque
        operacao = int(input())
    else:
        if total_estoque > operacao:
            total_estoque = total_estoque + operacao
            quantidade_vendas = quantidade_vendas + 1
            operacao = int(input())
        else:
            operacao = -operacao
            errosArray.append(f'Quantidade indisponível para a venda de {operacao} unidades.')
            operacao = int(input())
            
if len(errosArray) > 0:
    for erro in errosArray:
        print(erro)

print(f"Quantidade de vendas realizadas:{quantidade_vendas}")
print(f"Quantidade em estoque:{total_estoque}")
# impressão da saída
