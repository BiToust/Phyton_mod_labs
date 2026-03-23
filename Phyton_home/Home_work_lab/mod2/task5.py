# Ввод доменного имени
s = input()

# Собираю части вручную (split нельзя)
parts = []
current = ""

for ch in s:
    if ch == '.':
        parts.append(current)
        current = ""
    else:
        current += ch

# Добавляю последнюю часть
parts.append(current)

# Выводим в обратном порядке
for i in range(len(parts) - 1, -1, -1):
    print(parts[i])
