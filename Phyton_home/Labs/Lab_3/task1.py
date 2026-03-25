import requests

# Ввод города
city = input("Введите название города: ")

# URL и параметры
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "units": "metric",
    "lang": "ru",
    "appid": "79d1ca96933b0328e1c7e3e7a26cb347"   # токен
}

# Запрос
weather_data = requests.get(url, params=params).json()

# Проверка на ошибки
if weather_data.get("cod") != 200:
    print("Город не найден или ошибка запроса.")
else:
    # Извлекаем данные
    temp = round(weather_data["main"]["temp"])
    feels = round(weather_data["main"]["feels_like"])
    wind = weather_data["wind"]["speed"]
    pressure = weather_data["main"]["pressure"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    # Вывод
    print(f"\nПогода в городе {city}:")
    print(f"Температура: {temp}°C")
    print(f"Ощущается как: {feels}°C")
    print(f"Ветер: {wind} м/с")
    print(f"Давление: {pressure} гПа")
    print(f"Влажность: {humidity}%")
    print(f"Состояние: {description}")
