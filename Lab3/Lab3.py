from math import log10

COUNT_OF_ITERATIONS=0

def f(x:float) -> float:
    '''Функція, розв'язки якої шукаються'''
    return x*log10(x+1)-0.5

def bisection_method(start:float, end:float, e:float, g=f) -> float:
    '''Функція повертає роз'язок рівняння g(x)=0 знайдений на проміжку (start; end)
       методом ділення навпіл(методом бісекції)
    '''
    assert g(start)*g(end)<0
    middle=(start+end)/2
    while(abs(start-end)>e):
        print("Ліва границя відрізка:{0:<15}".format(round(start,7)),end="")
        print("Середина відрізка:{0:<15}".format(round(middle,7)),end="")
        print("Права границя відрізка:{0:<15}".format(round(end,7)))
        if g(start)*g(middle)<0:
            end=middle
        else:#g(middle)*g(end)<0
            start=middle
        middle=(start+end)/2
    return middle

def simple_iteration_method(x: float, e:float, g=f) -> float:
    '''Функція повертає роз'язок рівняння g(x)=0 знайдений в околі точки х
       методом послідовних наближень(методом простої ітерації)
       Для послідовнох наближеня використано формулу x_n+1 = -x_n * g(x_n) +  x_n
    '''
    global COUNT_OF_ITERATIONS
    COUNT_OF_ITERATIONS=1
    previous_point=x
    print("Біжуча точка:{0:.10f}".format(previous_point))
    next_point=-previous_point*g(previous_point)+previous_point
    while abs(next_point-previous_point)>e:
        previous_point=next_point
        print("Біжуча точка:{0:.10f}".format(previous_point))
        next_point=-previous_point*g(previous_point)+previous_point
        COUNT_OF_ITERATIONS+=1
    return next_point


eps=float(input("Введіть точність для методу ділення навпіл: "))
print("Метод ділення навпіл:")
x1=bisection_method(-0.8,-0.5,eps)
print("Перший корінь: ", x1, end='\n\n')
x2=bisection_method(1,2,eps)
print("Другий корінь: ", x2)
print("Вектор нев'язки: ( {0:.10f}, {1:.10f})".format(0-f(x1),0-f(x2)), end="\n\n")

eps=float(input("Введіть точність для уточнення розв'язків методом простої ітерації: "))
print("Метод простої ітерації:")
x3=simple_iteration_method(x1,eps)
print("Перший корінь: ", x3)
print("Кількість ітерацій: ",COUNT_OF_ITERATIONS, end='\n\n')
x4=simple_iteration_method(x2,eps)
print("Другий корінь: ", x4)
print("Кількість ітерацій: ",COUNT_OF_ITERATIONS)
print("Вектор нев'язки: ( {0:.10f}, {1:.10f})".format(0-f(x3),0-f(x4)), end="\n\n")


