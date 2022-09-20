from email.mime import base


def soma_valores(a, b):
    return a + b


def soma_valores_teste():
    a = [1,2,3,4,5,6,7,8,9,10]
    b = [1,2,3,4,5,6,7,8,9,10]
    
    for i in range(10):
        print(soma_valores(a[i], b[i]))
        
soma_valores_teste()

        