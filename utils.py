import requests

def weather_wttr(city):
    url = f"https://wttr.in/{city}?format=%C+%t+%w+%h&m"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Погода в {city}: {response.text}")
        else:
            print("Город не найден")
    except Exception as e:
        print(f"Ошибка: {e}")
