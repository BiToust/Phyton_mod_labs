import re

# Регулярка для даты и времени XXI века
pattern = r"2\d{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d"

# Ввод текста 
text = input("Введите текст для поиска в нём даты и времени (ГГГГ-ММ-ДД ЧЧ:ММ:СС):\n")

# Поиск совпадений
matches = re.finditer(pattern, text)

print("\nНайдено:")
found = False
for m in matches:
    print(m.group())
    found = True

if not found:
    print("Нет совпадений по дате и времени.")
