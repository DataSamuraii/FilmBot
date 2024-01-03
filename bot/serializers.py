from rest_framework import serializers
from .models import TelegramUser, Film, FilmRating


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['name', 'surname', 'tg_username', 'tg_id']


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmRating
        fields = ['user', 'film', 'rating']
