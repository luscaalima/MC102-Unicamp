###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Lucas Lima Pinheiro 
# RA: 263267
###################################################

# Leitura de dados
estoque = {
'nomeProduto':[],
'quantidadeProduto':[], 
'quantidadeCompras':[], 
'quantidadeVendas':[] 
}
qntProduto=[]
nomes=[]

while True:
  entrada = input() 
  if entrada.upper() =="FIM":
   break
  else :
    nomeProduto = (entrada.split(':')[0]).rstrip()
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
          qntProduto.append(str(-quantidadeProduto) )
          nomes.append(str(nomeProduto))
    
      else: 
       qntProduto.append(str(-quantidadeProduto) )
       nomes.append(str(nomeProduto))
    
    
if len(qntProduto)>0:
#  print('nomes',nomes)
#  print('qntProduto',qntProduto)
 indice = 0
 for nome in  nomes:
   index=nomes.index(nome)
   X=str(qntProduto[indice])
   N=nome
   print("Quantidade indisponivel para a venda de "+ X +" unidade(s) do produto "+ N + ".")
   indice = indice+1
   
oldArrayProduto = estoque['nomeProduto'][:]
estoque['nomeProduto'].sort()

   
for produto in estoque['nomeProduto']:
 index =oldArrayProduto.index(produto)
 N= produto
 E= str(estoque['quantidadeProduto'][index])
 C= str(estoque['quantidadeCompras'][index])
 V=str(estoque['quantidadeVendas'][index])
 print("Produto: " + N)
 print("Quantidade em Estoque: " + E)
 print("Pedidos de Compra: " + C)
 print("Pedidos de Venda: " + V)