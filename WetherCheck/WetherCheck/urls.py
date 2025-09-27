"""
URL configuration for WetherCheck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Імпортуємо адміністративну панель Django
from django.urls import path, include  # Імпорт для створення URL-шляхів
from Dweather import views  # Імпортуємо наші view-функції з додатку Dweather

# Список URL-шляхів для проекту
urlpatterns = [
    path('admin/', admin.site.urls),  # Стандартна сторінка адмінки Django
    path('', views.home, name='home'),  # Головна сторінка сайту
    path('register/', views.register, name='register'),  # Сторінка реєстрації
    path('login/', views.login_view, name='login'),  # Сторінка входу
    path('logout/', views.logout_view, name='logout'),  # Вихід користувача
    path('history/', views.history, name='history'),  # Сторінка історії пошуку
    path('search/', views.search_page, name='search_page'), # URL для показу сторінки пошуку погоди


]
