# задача 2

a = float(input('Введите число a: '))
b = float(input('Введите число b: '))

ch = a / b
inter = int(ch)
ost = a % b
print('При делении первого введеного числа на второе получилось', ch, ', целая часть', inter, ', остаток', ost)
ch = b / a
inter = int(ch)
oct = b % a
print('При делении второго введенного числа на первое получилос', ch, ', целая часть', inter, ', остаток', oct)

