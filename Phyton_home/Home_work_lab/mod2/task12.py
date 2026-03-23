# Ввод строки
s = input()

# Собираю строку без пробелов
res = ""
for ch in s:
    if ch != ' ':
        res += ch

print(res)
