from django.db import models

# TODO TG user with preferred genres, actors, years, countries


class TelegramUser(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True, null=True)
    tg_username = models.CharField(max_length=100, blank=True, null=True)
    tg_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Film(models.Model):
    title = models.CharField(max_length=200, unique=True)
    poster_url = models.URLField()
    release_date = models.DateField()
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    actors = models.TextField()  # Assuming there might be many actors
    age_limit = models.CharField(max_length=10)
    recommendations = models.TextField()  # List of recommended movies titles

    def __str__(self):
        return self.title


class FilmRating(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
