from rest_framework import serializers
from .models import TelegramUser, TelegramUserState, Film, FilmRating


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['name', 'surname', 'tg_username', 'tg_id']


class TelegramUserStateSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        chat_id = self.validated_data.get('chat_id')
        state = self.validated_data.get('state')

        instance, created = TelegramUserState.objects.update_or_create(
            chat_id=chat_id,
            defaults={'state': state}
        )
        return instance

    class Meta:
        model = TelegramUserState
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmRating
        fields = ['user', 'film', 'rating']
