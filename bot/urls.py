from django.urls import path
from .views import FilmList, FilmDetail, FilmRatingList, FilmRatingDetail, TelegramUserList, TelegramUserDetail, \
    TelegramUserStateList, TelegramUserStateDetail

urlpatterns = [
    path('films/', FilmList.as_view(), name='film_list'),
    path('films/<int:pk>/', FilmDetail.as_view(), name='film_detail'),
    path('film_ratings/', FilmRatingList.as_view(), name='film_rating_list'),
    path('film_ratings/<int:pk>/', FilmRatingDetail.as_view(), name='film_rating_detail'),
    path('telegram_users/', TelegramUserList.as_view(), name='telegram_user_list'),
    path('telegram_users/<int:pk>/', TelegramUserDetail.as_view(), name='telegram_user_detail'),
    path('user_states/', TelegramUserStateList.as_view(), name='user_state_list'),
    path('user_states/<int:pk>/', TelegramUserStateDetail.as_view(), name='user_state_detail'),
]
