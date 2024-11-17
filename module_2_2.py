first = int(input('Введите первое число: '))
print(first)
second = int(input('Введите второе число: '))
print(second)
third = int(input('Введите третье число: '))
print(third)
print('Число совпадений: ')
if first == second == third:
    print(3)
elif first != second != third:
    print(0)
elif first == second:
    print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)

