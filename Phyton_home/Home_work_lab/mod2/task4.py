# Ввод числа
s = input()

# Проверяю, что число натуральное (только цифры)
is_nat = True
for ch in s:
    if not ('0' <= ch <= '9'):
        is_nat = False
        break

if not is_nat or s == "0":
    print("Неверный ввод")
else:
    n = int(s)

    # Функция перевода в систему счисления (основание base)
    def to_base(num, base):
        digits = "0123456789ABCDEF"
        result = ""

        # Строю строку с конца
        while num > 0:
            r = num % base
            result = digits[r] + result
            num //= base

        return result

    b2 = to_base(n, 2)
    b8 = to_base(n, 8)
    b16 = to_base(n, 16)

    print(f"{b2}, {b8}, {b16}")
