import numpy as np

A=np.array([[0.49, 0, -0.128, 0.09, 0.15],
            [-0.03, 0.32, 0, -0.061, 0.02],
            [0.01, -0.09, 0.58, 0.011, 0.035],
            [0.03, 0, -0.073, 0.58, 0],
            [0.02, -0.03, 0.145, -0.012, 0.42]])

f=np.array([0.964, 1.279, -1.799, -4.971, 2.153])

eps=float(input("Введіть точність: "))
x=np.zeros(5)#вектор початкових наближень
i=1#початок першої ітерації
xnext=x-np.dot(A,x)+f
norma=np.absolute(x-xnext).max()#norma=max|xi-x(i+1)|
x=xnext
while norma>eps:
    i+=1
    xnext=x-np.dot(A,x)+f
    norma=np.absolute(x-xnext).max()#norm=max|xi-x(i+1)|
    x=xnext

r=np.dot(A,x)-f

print("Отримані розв'язки: ")
print("x0=",x[0])
print("x1=",x[1])
print("x2=",x[2])
print("x3=",x[3])
print("x4=",x[4])
print("Кількість ітерацій: ", i)
print("Вектор нев'язки: ")
print("r0={:.15f}".format(r[0]))
print("r1={:.15f}".format(r[1]))
print("r2={:.15f}".format(r[2]))
print("r3={:.15f}".format(r[3]))
print("r4={:.15f}".format(r[4]))
input()

