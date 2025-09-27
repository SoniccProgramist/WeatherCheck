import requests
from django.conf import settings

class OpenWeatherMap():
    def __init__(self, city):
        # Беремо ключ API з налаштувань
        self.api_key = settings.OPENWEATHERMAP_API_KEY
        # Завантажуємо дані про погоду для заданого міста
        self.data = self.get_data(city)

    def get_data(self, city):
        # Запит до OpenWeatherMap API
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}")
        d = response.json()
        # Якщо статус не 200, значить місто не знайдено
        if response.status_code != 200:
            raise ValueError(f"Місто '{city}' не знайдено. Спробуйте інше.")
        return d

    def get_wind(self):
        # Повертаємо швидкість вітру
        return self.get_any_key('wind', 'speed')

    def get_city(self):
        # Повертаємо назву міста
        return self.get_any_key('name')

    def get_temp(self):
        # Повертаємо температуру в градусах Цельсія
        temp = round(float(self.data.get('main')['temp']) - 273.15, 1)
        return temp

    def get_weather(self):
        # Повертаємо опис погоди (ясно, дощ тощо)
        weather = self.get_any_key('weather', 0, 'main')
        return weather

    def set_weather_info(self):
        # Виводимо інформацію про погоду у консоль
        print(f"Today weather in {self.get_any_key('name')} is {self.get_weather()}.Temperature is {self.get_temp()} °C")

    def get_text(self):
        # Формуємо текст для виводу з інформацією про погоду
        return (f"Місто: {self.get_city()}\n"
                f"Температура: {self.get_temp()}°C\n"
                f"Погода: {self.get_weather()}\n"
                f"Вітер: {self.get_wind()} м/с")

    def __str__(self):
        # Повертає рядок з основною інформацією
        return f"{self.get_city()}: {self.get_temp()}°C, {self.get_weather()}, {self.get_wind()} м/с"

    def get_any_key(self, *args):
        # Допоміжний метод, щоб дістати значення з вкладеного словника
        value = self.data
        for key in args:
            value = value[key]
        return value

def your_city_weather():
    # Простий приклад використання класу в консолі
    try:
        city_name = str(input("Введіть ваше місто англійською - "))
        print(OpenWeatherMap(city_name).get_text())
    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    your_city_weather()
