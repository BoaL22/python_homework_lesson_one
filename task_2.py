
    # Задача 2: Найдите сумму цифр трехзначного числа.

num = input('Введите трёхзначное число: ')

if len(num) < 3 or len(num) > 3:  print('Это не трёхзначное число! ')
else:   print(int(num[0]) + int(num[1]) + int(num[2]))
