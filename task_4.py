
    # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
    # Вместе они сделали S журавликов. 
    # Сколько журавликов сделал каждый ребенок, если известно, 
    # что Петя и Сережа сделали одинаковое количество журавликов, 
    # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

num = int(input('Сколько журавликов было сделано? '))

cranes = num / 4
Petr = cranes
Katya = cranes * 2
Sergey = cranes

print(f'\n Петя сделал - {Petr} журавликов\n Катя - {Katya} журавликов\n Сережа - {Sergey} журавликов')
