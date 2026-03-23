# Ввод строки из нулей и единиц
s = input()

zeros = 0
ones = 0

# Считаю вручную, count нельзя
for ch in s:
    if ch == '0':
        zeros += 1
    elif ch == '1':
        ones += 1

# Сравниваю
if zeros == ones:
    print("yes")
else:
    print("no")
