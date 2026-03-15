from utils import weather_wttr


def say_hi():
    print('hello world')

def main():
    city = 'Мытищи'
    say_hi()
    weather_wttr(city)

if __name__ == '__main__':
    main()