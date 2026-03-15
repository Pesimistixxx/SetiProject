import requests
import xml.etree.ElementTree as ET


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


def get_cbr_rates():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"

    try:
        response = requests.get(url)
        response.encoding = 'windows-1251'

        root = ET.fromstring(response.text)

        date = root.get('Date')
        print(f"\n{'=' * 50}")
        print(f"Курсы валют ЦБ РФ на {date}")
        print(f"{'=' * 50}")

        currencies = {
            'USD': 'Доллар США',
            'EUR': 'Евро',
        }

        for valute in root.findall('Valute'):
            char_code = valute.find('CharCode').text
            if char_code in currencies:
                name = valute.find('Name').text
                value = valute.find('Value').text
                nominal = valute.find('Nominal').text

                value = float(value.replace(',', '.'))

                print(f"\n{char_code} - {currencies[char_code]}")
                print(f"  {nominal} {name}: {value} руб.")

    except Exception as e:
        print(f"Ошибка: {e}")
