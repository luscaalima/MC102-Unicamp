###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Lucas Lima Pinheiro 
# RA: 263267
###################################################

# Leitura de dados
estoque = {}

# print(  'entrada',entrada.split(':')[1])


while True:
  entrada = input() 
  nomeProduto = entrada.split(':')[0]
  quantidadeProduto = int(entrada.split(':')[1])
  if nomeProduto in estoque['nomeProduto']:
    pass
  item = {
    'nomeProduto': nomeProduto,
    'quantidadeProduto':quantidadeProduto
  }
  print('item',item)
  # estoque.update(item)
  print('estoque',estoque)
# Processamento
  if quantidadeProduto > 0:
    #COMPRA
    print('compra de ',quantidadeProduto,'unidades do produto',nomeProduto )
  else :
    print('venda  de ',-quantidadeProduto,'unidades do produto',nomeProduto )
  #...
# print("Quantidade indisponivel para a venda de " + X + " unidade(s) do produto " + N + ".")

# Impressão da saída
# ...
  # print("Produto: " + N)
  # print("Quantidade em Estoque: " + E)
  # print("Pedidos de Compra: " + C)
  # print("Pedidos de Venda: " + V)