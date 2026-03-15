from utils import weather_wttr, get_cbr_rates


def say_hi():
    print('hello world')

def say_bye():
    print('goodbye')

def main():
    city = 'Мытищи'
    say_hi()
    weather_wttr(city)
    get_cbr_rates()
    say_bye()

if __name__ == '__main__':
    main()