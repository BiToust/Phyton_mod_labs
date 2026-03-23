# Ввод трёх чисел через пробел (split нельзя, поэтому ищу пробелы вручную)
line = input()

# Ищу позиции двух пробелов
first_sp = -1
second_sp = -1

for i in range(len(line)):
    if line[i] == ' ':
        if first_sp == -1:
            first_sp = i
        else:
            second_sp = i
            break

# Разбираю три числа вручную
a = int(line[:first_sp])
b = int(line[first_sp + 1:second_sp])
c = int(line[second_sp + 1:])

# Логика поиска среднего: число, которое не минимальное и не максимальное
if (a <= b <= c) or (c <= b <= a):
    mid = b
elif (b <= a <= c) or (c <= a <= b):
    mid = a
else:
    mid = c

print(mid)
