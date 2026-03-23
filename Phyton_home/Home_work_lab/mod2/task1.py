# Вводим строку формата "a, b"
s = input()

# Ищу позицию запятой вручную, т.к. split использовать нельзя
comma_pos = -1
for i in range(len(s)):
    if s[i] == ',':
        comma_pos = i
        break

# Беру первое число — всё, что до запятой
a = int(s[:comma_pos])

# Беру второе число — после запятой и пробела
b = int(s[comma_pos + 2:])

# Остаток от деления
result = a % b

print(result)
