import numpy as np

A=np.array([[0.49, 0, -0.128, 0.09, 0.15],
            [-0.03, 0.32, 0, -0.061, 0.02],
            [0.01, -0.09, 0.58, 0.011, 0.035],
            [0.03, 0, -0.073, 0.58, 0],
            [0.02, -0.03, 0.145, -0.012, 0.42]])
A1=np.tril(A,k=-1)#нижня трикутна матриця
A2=np.triu(A,k=1)#верхня трикутни матриця
D=np.diag(np.diag(A))#діагональна матриця

f=np.array([0.964, 1.279, -1.799, -4.971, 2.153])

eps=float(input("Введіть точність: "))
x=np.zeros(5)#вектор початкових наближень
i=1#початок першої ітерації
Left=(-1)*np.linalg.inv(D)
Right=np.dot(A1,x)+np.dot(A2,x)-f
xnext=np.dot(Left,Right)
norma=np.absolute(x-xnext).max()#norma=max|xi-x(i+1)|
x=xnext
while norma>eps:
    i+=1
    Left=(-1)*np.linalg.inv(D)
    Right=np.dot(A1,x)+np.dot(A2,x)-f
    xnext=np.dot(Left,Right)
    norma=np.absolute(x-xnext).max()#norma=max|xi-x(i+1)|
    x=xnext

r=np.dot(A,x)-f


print("Отримані розв'язки: ")
for j in range(5):
    print("x{}={}".format(j,x[j]))
print("Кількість ітерацій: ", i)
print("Вектор нев'язки: ")
for j in range(5):
    print("r{}={:.15f}".format(j,r[j]))
input()

