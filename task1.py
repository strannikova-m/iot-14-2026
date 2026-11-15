from enum import Enum
class Type(Enum):
    SUNNY = 1
    CLOUDY = 2
    RAINY = 3
    FOGGY = 4
    SNOWY = 5
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Починаємо")
        print("Передані аргументи:", args)
        print("Передані додаткові параметри:", kwargs)
        func(*args, **kwargs)
        print("Закінчили")
    return wrapper

class Weather:
    def __init__(self, day, city, country, temp, humidity, wind_speed, type):
        self.day = day
        self.city = city
        self.country = country
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.type = type

    def __del__(self):
        print("Запис видалено:", self.day, self.city)

    def get_day(self):
        return self.day

    def get_temp(self):
        return self.temp

    def set_temp(self, temp):
        self.temp = temp

    def show(self):
        print("День", self.day, self.city, self.country, self.temp, "°C",
              self.humidity, "%", self.wind_speed, "м/с", self.type.name)

    def is_lviv_weather(self, humidity, type):
        if humidity > 80 and type == Type.RAINY:
            print("The typical day in Lviv")
        else:
            print("You're lucky, man")


class WeatherCalendar:
    def __init__(self):
        self.records = []
    def add(self, weather):
        self.records.append(weather)

    def show(self):
        for w in self.records:
            w.show()

    def sort_by_day(self):
        self.records.sort(key=lambda w: w.day)
@decorator
def find_max_temperature(records, day):
    max_temp = None
    for w in records:
        if w.day == day:
            if max_temp is None or w.temp > max_temp:
                max_temp = w.temp
    if max_temp is None:
        print("Max temperature on day", day, "=", "Not enough data")
    else:
        print("Max temperature on day", day, "=", max_temp)


def main():
    calendar = WeatherCalendar()
    calendar.add(Weather(3, "Lviv", "Ukraine", 8, 85, 4, Type.RAINY))
    calendar.add(Weather(1, "Kyiv", "Ukraine", 12, 60, 3, Type.SUNNY))
    calendar.add(Weather(3, "Odesa", "Ukraine", 14, 55, 5, Type.CLOUDY))

    print("Погода")
    calendar.show()

    print("Максимальна температура")
    find_max_temperature(calendar.records, 3)
    find_max_temperature(calendar.records, 10)
    find_max_temperature(records=calendar.records, day=3)

    print("Типова погода Львова?")
    for w in calendar.records:
        print(w.city, end=" ")
        w.is_lviv_weather(w.humidity, w.type)

    print("Сортування")
    calendar.sort_by_day()
    calendar.show()


main()