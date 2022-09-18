import math

while True:
    f1='f1-сложение(a+b),'
    f2='f2-вычитание(a-b),'
    f3='f3-умножение(a*b),'
    f4='f4-деление(a/b),'
    f5='f5-возведение в степень(a^b),'
    f6='f6-значение логарифма(loga(b),log по основанию a числа b),'
    f7='f7-округление в большую сторону до b знака после запятой(a-округляемое число),'
    f8='f8-округление в меньшую сторону до b знака после запятой(a-округляемое число).'
    print("ФУНКЦИИ:",f1,f2,f3,f4,f5,f6,f7,f8)
    f=input("Выберите нужную функцию:")
    try:
        a=(input("Введите первое число 'a':"))
        b=int((input("Введите второе число 'b':")))
        if f=="f1":
            print("Ответ:",int(a)+b)
        elif f=="f2":
            print("Ответ:",int(a)-b)
        elif f=="f3":
            print("Ответ:",int(a)*b)
        elif f=="f4":
            if b!=0:
                print("Ответ:",int(a)/b)
            else:
                print("Ошибка")
        elif f=="f5":
            print("Ответ:",int(a)**b)
        elif f=="f6":
            print("Ответ:",math.log(b,int(a)))
        elif f=="f7":
            a=float(a)
            miltiplier=10**b
            print(math.ceil(a*miltiplier)/miltiplier)
        elif f=="f8":
            a=float(a)
            miltiplier=10**b
            print(math.floor(a*miltiplier)/miltiplier)
    except:
        print("ОШИБКА!Введите корректные данные.")
