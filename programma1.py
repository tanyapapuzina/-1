#Задание №1(команда с числом и команда со словом)
print("Для нахождения вашего возраста введите следующие числа:")
birth=int(input("год вашего рождения:"))
year=int(input("нынешний год:"))
answer=input("В этом году у вас уже было день рождение? Напишите 'да' или 'нет':")
if answer=="да":
    age=year-birth
else:
    age=year-birth-1
print("Возраст:",age)
#Задание №1(команда со строкой)
number=int(input("Введите в строку количество букв вашего имени:"))
a1=input("Введите первую букву вашего имени:")
name=[a1]
while number>1:
    name.append(input("Введите следующую букву вашего имени:"))
    number-=1
name=''.join(name)
print("Ваше имя будет записно как:", name)
#Задание №1(команда со списком)
information=list()
information.append(name)
information.append(age)
print("Ваши данные:",information)
#Задание №1(команда с кортежем)
inf=tuple(information)
print("Имя:",inf[0],"; Возраст:", inf[1])
