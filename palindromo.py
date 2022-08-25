palavra = input('Digite uma palavra: ').lower().strip().replace(' ', '')
if palavra == palavra[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')