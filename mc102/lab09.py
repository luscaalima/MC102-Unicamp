###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Lucas Lima Pinheiro 
# RA: 263267
###################################################

# Leitura de dados
# estoque = {}
# print('estoque',len(estoque))

# print(  'entrada',entrada.split(':')[1])


estoque = {
'nomeProduto':[
  'LUCAS'
  ],
'quantidadeProduto':[8]  
}
  
# print ('type',type(estoque))
while True:
  entrada = input() 
  if entrada.upper() =="FIM":
   break
  else :
    nomeProduto = entrada.split(':')[0]
    # X
    quantidadeProduto = int(entrada.split(':')[1])
    if quantidadeProduto > 0 :
      print('nomeProduto',estoque['nomeProduto'])
      print( 'if ',nomeProduto in estoque['nomeProduto'])
      if nomeProduto in estoque['nomeProduto']:
        #Altera quantidadeProduto
        index =estoque['nomeProduto'].index(nomeProduto)
        estoque['quantidadeProduto'][index]= quantidadeProduto
      else: 
        estoque['nomeProduto'].append(nomeProduto)
        estoque['quantidadeProduto'].append(quantidadeProduto)
     #  isso indica um  pedido de compra de X unidades do produto N para reposição do estoque
    else:
      if nomeProduto in estoque['nomeProduto']:
        #Altera quantidadeProduto
        index =estoque['nomeProduto'].index(nomeProduto)
        estoque['quantidadeProduto'][index]= quantidadeProduto
      else: 
        index = estoque['nomeProduto'].index(nomeProduto)
        if  (-quantidadeProduto) > estoque['quantidadeProduto'][index]:
          # tirando do estoque mais do que tem ???
          #"Quantidade indisponivel para a venda de " + quantidadeProduto + " unidade(s) do produto " + nomeProduto + "."
         print("Quantidade indisponivel para a venda de " + (-quantidadeProduto) + " unidade(s) do produto " + nomeProduto + ".")
    
    
    
    
    
    
    
      # caso contrário, isso indica um pedido de venda de X unidades do produto N
    
    # print('nomeProduto', nomeProduto)
    # print('quantidadeProduto', quantidadeProduto)
    
 
    #  estoque.update( new_estoque)
  # estoque.update(item) print('estoque',estoque)
# # Processamento
#   if quantidadeProduto > 0:
#     #COMPRA
#     print('compra de ',quantidadeProduto,'unidades do produto',nomeProduto )
#   else :
#     print('venda  de ',-quantidadeProduto,'unidades do produto',nomeProduto )
  #...
# print("Quantidade indisponivel para a venda de " + X + " unidade(s) do produto " + N + ".")

# Impressão da saída
# ...
  # print("Produto: " + N)
  # print("Quantidade em Estoque: " + E)
  # print("Pedidos de Compra: " + C)
  # print("Pedidos de Venda: " + V)