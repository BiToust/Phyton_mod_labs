# Ввод строки со словами
s = input()

# Разбиваю вручную (split нельзя)
words = []
cur = ""

for ch in s:
    if ch == ' ':
        words.append(cur)
        cur = ""
    else:
        cur += ch

words.append(cur)

# Собираю слово из последних букв
result = ""
for w in words:
    if len(w) > 0:
        result += w[-1]

print(result)
