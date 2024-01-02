from django.db import models

# TODO TG user with preferred genres, actors, years, countries


class TelegramUser(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    tg_username = models.CharField(max_length=100, blank=True, null=True)
    tg_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
