from django.http import JsonResponse
from rest_framework import generics, filters
from rest_framework import status

from .models import Film, FilmRating, TelegramUser, TelegramUserState
from .serializers import FilmSerializer, FilmRatingSerializer, TelegramUserSerializer, TelegramUserStateSerializer


# Views for TelegramUser
class TelegramUserList(generics.ListCreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer

    def post(self, request, *args, **kwargs):
        tg_id = request.data.get('tg_id')
        try:
            user, created = TelegramUser.objects.get_or_create(tg_id=tg_id, defaults=request.data)
            if not created:
                # Update existing user with new data if needed
                for key, value in request.data.items():
                    setattr(user, key, value)
                user.save()
            serializer = self.get_serializer(user)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TelegramUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer


class TelegramUserStateList(generics.ListCreateAPIView):
    queryset = TelegramUserState.objects.all()
    serializer_class = TelegramUserStateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['chat_id']

    def post(self, request, *args, **kwargs):
        chat_id = request.data.get('chat_id')
        try:
            user_state, created = TelegramUserState.objects.get_or_create(chat_id=chat_id, defaults=request.data)
            if not created:
                # Update existing user state with new data
                for key, value in request.data.items():
                    setattr(user_state, key, value)
                user_state.save()
            serializer = self.get_serializer(user_state)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
