from django.contrib import admin
from .models import SearchHistory
# Реєструємо модель, щоб бачити її в адмінці
@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'created_at')  # Що показувати в списку
    list_filter = ('created_at',)  # Фільтр по даті
    search_fields = ('user__username', 'city')  # Можливість шукати по користувачу або місту
    ordering = ('-created_at',)  # Сортування від останніх пошуків