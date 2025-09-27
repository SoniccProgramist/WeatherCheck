from django.db import models  # Імпортуємо моделі Django для створення таблиць
from django.contrib.auth.models import User  # Імпорт моделі користувача

# Модель для збереження історії пошуку користувачів
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Посилання на користувача, який зробив пошук
    city = models.CharField(max_length=100)  # Назва міста, яке шукали
    created_at = models.DateTimeField(auto_now_add=True)  # Дата і час створення запису (автоматично)

    def __str__(self):
        # Як буде відображатися запис в адмінці або в консолі
        return f"{self.user.username} - {self.city}"