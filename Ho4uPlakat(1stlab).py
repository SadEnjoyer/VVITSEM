print('Введите коэффициенты уравнения вида ax^2+bx+c=0')
print('Введите коэффициент a')
try:
    a = float(input())
    print('Введите коэффициент b')
    b = float(input())
    print('Введите коэффициент c')
    c = float(input())
    d = b**2 - 4*a*c
    if d < 0 :
        print('Корней нет')
    elif d == 0:
        x = -b/(2*a)
        print(f'Единственный корень {x}')
    else:
        x1 = (-b+d**0.5)/(2*a)
        x2 = (-b-d**0.5)/(2*a)
        print(f'Найденные корни равны {x1} и {x2}')
except (ValueError,ZeroDivisionError):
        print('Не ломайте код :(')
