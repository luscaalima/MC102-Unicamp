import numpy as np

a = np.array(
    [
        [1,3,2],
        [4,5,3],
        [1,7,0]
    ]
    )
# inversa_a = np.array(
#     [
#         [(-21/34),7/17,(-1/34)],
#         [ 3/34,(-1/17),5/34],
#         [23/34,(-2/17),(-7/34)]
#     ]
#     )

# a = np.array(
#     [
#         [1,1,1],
#         [2,2,2],
#         [1,7,0]
#     ]
#     )
print('A')
for linha in a : 
    print(linha)

print('\n')
    
print('A^T')
for linha in a.T : 
    print(linha)    

print('\n')

print('\n')
    
print('Determinante de A',np.linalg.det(a))  
if np.linalg.det(a)!= 0:
    print('\n')    
    print('A^-1')
    for linha_inversa in np.linalg.inv(a):
        print(linha_inversa)
    
    inversa = np.linalg.inv(a)
    print('##',np.dot(a,inversa) == np.eye(3))   
    
    
  
# inversa_a =np.linalg.inv(a)    
# print('A X A^(-1)',a@inversa_a  == np.eye(3)  )    

#CRIA MATRIZ IDENTIDADE DE ORDEM N
# print('\n')    
# n = int(input("Identidade de N: "))

# print("\n")
# for linha in np.eye(n):
#     print(linha)

# print('D x D^(-1)',identidade)
# # A X A^-1 = I 
# print('--->',np.dot(d,np.linalg.inv(d)) == np.eye(2)  )