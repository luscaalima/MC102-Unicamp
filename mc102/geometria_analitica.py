import numpy as np

a = np.array([[1, 3, 2], [4,5,3]])
#print(a)
b = np.array([[2, 1, 4], [9, 5, 2]])
c = np.array([[2, 1], [9, 5],[4,2]])
print('-------------------------------------------')
print(c)
print('-------------------------------------------')
# print('A x C',np.dot(a,c))
print()
# a + b
# print(a+b)
# A x B 
# np.dot(a,b)
# print('AxB')

d = np.array([[3,2],[3,4]])
print('matriz d',d)
print( 'transposta',d.T )
print('inversa',np.linalg.inv(d))
# A X A^-1 = I 
print('--->',np.dot(d,np.linalg.inv(d)) == np.eye(2)  )
