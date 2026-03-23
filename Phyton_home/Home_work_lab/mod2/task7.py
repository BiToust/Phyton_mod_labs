# Ввод строки и символа через запятую
s = input()

# Ищу запятую
comma = -1
for i in range(len(s)):
    if s[i] == ',':
        comma = i
        break

text = s[:comma]
symbol = s[comma + 1:]  # без пробела по условию

# Считаю, сколько раз символ стоит в начале строки
count = 0
for ch in text:
    if ch == symbol:
        count += 1
    else:
        break

print(count)
