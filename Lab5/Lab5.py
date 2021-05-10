def divided_differences(X:list,F:list)->list:
    """Функція, що повертає таблицю(список списків) розділених різниць"""
    tabl=[[0]*(len(X)-i) for i in range(len(X))]
    for i in range(len(F)):
        tabl[i][0]=F[i]
    for j in range(1,len(tabl)):
        for i in range(len(tabl)-j):
            tabl[i][j]=(tabl[i+1][j-1]-tabl[i][j-1])/(X[i+j]-X[i])
    return tabl

def newtons_polynomial(x:float,tabl:list,X:list)->float:
    """Обчислення значення полінома Нютона в точці х"""
    sum=tabl[0][0]
    for i in range(1,len(tabl)):
        addition=tabl[0][i]
        for j in range(i):
            addition*=(x-X[j])
        sum+=addition
    return sum

def show_table(tabl:list)->None:
    """Функція для виведення таблиці розділених різниць"""
    for i in range(len(tabl)):
        for j in range(len(tabl[i])):
            print("{:.10f}".format(tabl[i][j]),end="\t")
        print()

X=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
Y=[2, 1.95533, 1.82533, 1.6216, 1.36235, 1.07073, 0.77279, 0.49515, 0.2626, 0.09592]

tabl=divided_differences(X,Y)
print("Таблиця розділених різниць:")
show_table(tabl)
x1=newtons_polynomial(0.221, tabl, X)
x2=newtons_polynomial(0.408, tabl, X)
x3=newtons_polynomial(0.681, tabl, X)
print("Наближене значення функції у точці 0,221: ",x1)
print("Наближене значення функції у точці 0,408: ",x2)
print("Наближене значення функції у точці 0,681: ",x3)
