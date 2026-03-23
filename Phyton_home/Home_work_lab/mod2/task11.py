# Ввод строки
s = input()

# Проверяю вручную, без разворотов и функций
is_pal = True
left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        is_pal = False
        break
    left += 1
    right -= 1

print("yes" if is_pal else "no")
