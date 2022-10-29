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
'nomeProduto':[],
'quantidadeProduto':[], 
'quantidadeCompras':[], 
'quantidadeVendas':[] 
}
quantidadeIndisponivel=[]

while True:
  entrada = input() 
  if entrada.upper() =="FIM":
   break
  else :
    nomeProduto = (entrada.split(':')[0])
    # X
    quantidadeProduto = int(entrada.split(':')[1])
    if quantidadeProduto > 0 :
      #COMPRA DE X UNIDEADES
      if nomeProduto in estoque['nomeProduto']:
        #Altera quantidadeProduto
        index =estoque['nomeProduto'].index(nomeProduto)
        estoque['quantidadeProduto'][index]=int(estoque['quantidadeProduto'][index])+quantidadeProduto
        estoque['quantidadeCompras'][index] =  estoque['quantidadeCompras'][index] +1
      else: 
        # isso indica um  pedido de compra de X(quantidadeProduto) unidades do produto N(nomeProduto) para reposição do estoque
        estoque['nomeProduto'].append(nomeProduto)
        estoque['quantidadeProduto'].append(quantidadeProduto)
        estoque['quantidadeCompras'].append(1)
        estoque['quantidadeVendas'].append(0)
    
    else:
    
      if nomeProduto in estoque['nomeProduto']:
        #Altera quantidadeProduto
        index =estoque['nomeProduto'].index(nomeProduto)
        
        if (estoque['quantidadeProduto'][index]+quantidadeProduto) >= 0 :
          estoque['quantidadeProduto'][index]=int(estoque['quantidadeProduto'][index])+quantidadeProduto
          estoque['quantidadeVendas'][index] =  estoque['quantidadeVendas'][index] +1
          
        else :
          #converter quantidadeProduto
          # print("Quantidade indisponivel para a venda de " + str(-quantidadeProduto) + " unidade(s) do produto " + nomeProduto + ".")
          quantidadeIndisponivel.append("Quantidade indisponivel para a venda de " + str(-quantidadeProduto) + " unidade(s) do produto " + nomeProduto + ".")
    
      else: 
       quantidadeIndisponivel.append("Quantidade indisponivel para a venda de " + str(-quantidadeProduto) + " unidade(s) do produto " + nomeProduto + ".")
    
    
    # print('estoque',estoque)
  
  
print('type',type(estoque))  
print(estoque)     
    
if len(quantidadeIndisponivel)>0:
 for mensagem in  quantidadeIndisponivel :
   print(mensagem)
   

   
for produto in estoque['nomeProduto']:
 index =estoque['nomeProduto'].index(produto)
#  print('index:',index)
 
 print('Produto',estoque['nomeProduto'][index])    
#  print("Produto: " + N)
 E=estoque['quantidadeProduto'][index]
 print("Quantidade em Estoque: " + str(E))
 print("Pedidos de Compra: " + str(estoque['quantidadeCompras'][index]))
 print("Pedidos de Venda: " +str(estoque['quantidadeVendas'][index]))
    
 
    

# Impressão da saída
# ...
  # print("Produto: " + N)
  # print("Quantidade em Estoque: " + E)
  # print("Pedidos de Compra: " + C)
  # print("Pedidos de Venda: " + V)