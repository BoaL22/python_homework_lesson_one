
    # Задача 2: - HARD необязательная, идет за 3 обязательных 
    # Найдите сумму цифр любого вещественного или целого числа. 
    # Можно использовать decimal. Через строку решать нельзя.

number = input('Введите число! ')
num_one = number.replace('.', '')
num_two = num_one.replace(',', '')
list_str = list(num_two)
list_int = map(int, list_str)
list_win = sum(list_int)
print(list_win)


# from decimal import Decimal
# number = Decimal(input())
 
# digits = number.as_tuple().digits
# print(sum(digits))


# number = input('Enter a number: ')
# sum = 0
# i = 0
# while i < len(number):
#     if number[i] == '.':     i += 1
#     elif number[i] == ',':     i += 1
#     sum = sum + int(number[i]) 
#     i += 1
# print(sum)

# a = float(number) % 10
# a = float(number) // 10
# print(a)
