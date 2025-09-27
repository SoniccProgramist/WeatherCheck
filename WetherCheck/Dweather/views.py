from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SearchHistory
from .weather_api import OpenWeatherMap


def register(request):
    # реєстрація користувача
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # відразу логіним користувача
            messages.success(request, f"Реєстрація успішна! Ласкаво просимо, {user.username}.")
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "Dweather/register.html", {"form": form})


def login_view(request):
    # вхід користувача
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "Dweather/login.html", {"form": form})


def logout_view(request):
    # вихід користувача
    logout(request)
    return redirect("home")


def home(request):
    # головна сторінка
    if request.user.is_authenticated:
        return redirect("search_page")  # якщо авторизований, на пошук
    return render(request, "Dweather/home.html")


@login_required
def search_page(request):
    # беремо останні 3 пошуки користувача
    search_history = request.user.searchhistory_set.all().order_by('-created_at')[:3]

    weather_data = None
    city = None

    if request.method == "POST":
        city = request.POST.get("city")
        try:
            # виклик API
            weather_obj = OpenWeatherMap(city)
            weather_data = {
                'city': weather_obj.get_city(),
                'temp': weather_obj.get_temp(),
                'weather': weather_obj.get_weather(),
                'wind': weather_obj.get_wind(),
                'text': weather_obj.get_text(),
            }
            # зберігаємо пошук
            SearchHistory.objects.create(user=request.user, city=weather_data['city'])
            messages.info(request, f"Погода для міста {weather_data['city']} завантажена.")
        except ValueError as e:
            # якщо місто не знайдено
            messages.error(request, str(e))
        except Exception:
            # якщо сталася критична помилка
            messages.error(request, "Помилка при отриманні даних. Спробуйте пізніше.")

    context = {
        'search_history': search_history,
        'weather_data': weather_data,
        'city_searched': city,
    }
    return render(request, "Dweather/search_page.html", context)


@login_required
def history(request):
    # показуємо всю історію пошуків
    search_history = request.user.searchhistory_set.all().order_by('-created_at')
    return render(request, "Dweather/history.html", {'search_history': search_history})

