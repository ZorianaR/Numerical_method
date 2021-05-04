from math import log, log10

COUNT_OF_ITERATIONS=0

def f(x:float)->float:
    return x*log10(x+1)-0.5

def diff_f(x:float)->float:
    return log10(x+1)+(x/(log(10)*(x+1)))

def newtons_method(x_prev:float, eps:float)->float:
    """Функція для уточнення розв'язку, отриманого у попередній лабораторній, методом Нютона"""
    global COUNT_OF_ITERATIONS
    COUNT_OF_ITERATIONS=1#перша ітерація
    x_next=x_prev-(f(x_prev)/diff_f(x_prev))
    while abs(x_next-x_prev)>eps: 
        COUNT_OF_ITERATIONS+=1
        print("Біжуче значення x={:.20f}".format(x_next))
        x_prev=x_next
        x_next=x_prev-(f(x_prev)/diff_f(x_prev))
    return x_next

eps=float(input("Введіть точність: "))

x1=-0.77#знайдений у попередній роботі розв'язок
x2=1.348#знайдений у попередній роботі розв'язок
#x1=x1-(f(x1)/diff_f(x1))
x1=newtons_method(x1, eps)
print("Перший корінь: {:.20f}".format(x1))
print("Кількість ітерацій: ",COUNT_OF_ITERATIONS, end='\n\n')

x2=newtons_method(x2, eps)
print("Другий корінь: {:.20f}".format(x2))
print("Кількість ітерацій: ",COUNT_OF_ITERATIONS, end='\n\n')

print("Вектор нев'язки: ( {0:.20f}, {1:.20f})".format(0-f(x1),0-f(x2)))
