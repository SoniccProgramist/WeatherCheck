# WeatherCheck
Це мій перший проект на Django. Він показує погоду для будь-якого міста через API OpenWeatherMap.

Що вміє:

-Можна зареєструватися і увійти

-Пошук погоди по місту

-Історія всіх пошуків доступна на окремій сторінці

-Вихід з акаунта

# Як запускати

1.Клонуй репозиторій

2.Створи віртуальне середовище 
    
    python -m venv .venv

3.Активуй його

    Windows: .venv\Scripts\activate

    Linux/Mac: source .venv/bin/activate

4.Встанови бібліотеки

    pip install -r requirements.txt

5.Створи базу даних

    python manage.py migrate

6.Створи суперкористувача (щоб заходити в адмінку)

    python manage.py createsuperuser

7.Запусти сервер
    
    python manage.py runserver

# Файли

Dweather/ – додаток Django

templates/ – html сторінки

static/ – картинки і відео фонове

weather_api.py – тут працює API OpenWeatherMap

urls.py – шляхи для всіх сторінок

views.py – логіка для сторінок

models.py – історія пошуків користувача

# Примітки

1.Для пошуку погоди треба ключ API з OpenWeatherMap, його треба покласти в .env(OPENWEATHERMAP_API_KEY=ВАШ КЛЮЧ)
