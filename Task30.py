"""
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""
first_elem = int (input('Первый элемент арифм.прогрессии: '))
step = int (input ('Шаг прогрессии: '))
number_of_elements = int (input ('Число элементов прогрессии: '))

last_element = first_elem + (number_of_elements - 1 )* step
result = [num for num in range (first_elem, last_element + 1, step)]

print(*result)