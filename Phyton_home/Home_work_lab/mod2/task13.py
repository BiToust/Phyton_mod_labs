# Ввод числа как строки
s = input()

# Ищу максимальную цифру вручную
max_digit = '0'

for ch in s:
    if ch > max_digit:
        max_digit = ch

print(max_digit)
