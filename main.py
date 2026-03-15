from utils import weather_wttr, get_cbr_rates


def say_hi():
    print('hello world')

def main():
    city = 'Мытищи'
    say_hi()
    weather_wttr(city)
    get_cbr_rates()

if __name__ == '__main__':
    main()