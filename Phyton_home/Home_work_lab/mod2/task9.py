# Ввод строки с номером
s = input()

allowed = "+0123456789"
result = ""

# Оставляю только цифры и плюс
for ch in s:
    ok = False
    for a in allowed:
        if ch == a:
            ok = True
            break

    if ok:
        result += ch

print(result)
