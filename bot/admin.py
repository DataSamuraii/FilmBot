from django.contrib import admin

from .models import TelegramUser, TelegramUserState, Film


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TelegramUserState)
class TelegramUserStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass
