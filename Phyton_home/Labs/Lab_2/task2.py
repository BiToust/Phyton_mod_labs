import re

# Фильтр для поиска email-адресов
pattern = r"[a-zA-Z0-9+_\-#]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"

# Ввод текста
text = input("Введите текст для нахождения в них email-адресов:\n")

# Поиск совпадений
emails = re.findall(pattern, text)

print("\nПоиск email-адресов:")
if emails:
    for email in emails:
        print(email)
else:
    print("Email-адресов не найдено.")
