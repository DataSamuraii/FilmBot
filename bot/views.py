from rest_framework import generics
from .models import Film, FilmRating, TelegramUser, TelegramUserState
from .serializers import FilmSerializer, FilmRatingSerializer, TelegramUserSerializer, TelegramUserStateSerializer


# Views for TelegramUser
class TelegramUserList(generics.ListCreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer


class TelegramUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer


class TelegramUserStateList(generics.ListCreateAPIView):
    queryset = TelegramUserState.objects.all()
    serializer_class = TelegramUserStateSerializer


class TelegramUserStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TelegramUserState.objects.all()
    serializer_class = TelegramUserStateSerializer


# Views for Film
class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


# Views for FilmRating
class FilmRatingList(generics.ListCreateAPIView):
    queryset = FilmRating.objects.all()
    serializer_class = FilmRatingSerializer


class FilmRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilmRating.objects.all()
    serializer_class = FilmRatingSerializer
