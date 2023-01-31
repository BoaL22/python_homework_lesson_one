
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
