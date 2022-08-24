from IPython.display import display
import pandas as pd

# dataFrame = pd.DataFrame();
# venda = {'data': ['15/02/2021', '16/02/2021'],
#          'valor': [500, 300],
#          'produto': ['feijao', 'arroz'],
#          'qtde': [50, 70],
#          };


vendas_Df = pd.read_excel('Vendas.xlsx')
# display(vendas_Df)
# display(vendas_Df.head(10))
# print(vendas_Df.shape)
produtos = vendas_Df[['Produto','ID Loja']]
# display(produtos)
#pegar uma linha
display(vendas_Df.loc[1:5])