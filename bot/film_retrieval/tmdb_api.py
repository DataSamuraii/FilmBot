import requests
import os
from dotenv import load_dotenv

load_dotenv()
TMDb_API_KEY = os.getenv('TMDb_API_KEY')


def get_film_from_search(film_title):
    search_results = search_film(film_title)
    if not search_results:
        return []

    film = search_results.get('results', [])[0]
    details = get_film_details(film['id'])
    if details:
        film_cast = get_film_cast(film['id'])
        top_cast = [cast_member['name'] for cast_member in film_cast.get('cast', [])[:5]]

        film_ratings = get_film_ratings(film['id'])
        us_rating = next((rating['certification'] for country_ratings in film_ratings.get('results', [])
                          for rating in country_ratings['release_dates']
                          if country_ratings['iso_3166_1'] == 'US'), 'NR')

        similar_films = get_similar_films(film['id']).get('results')[:5]
        films_to_recommend = [film.get('title') for film in similar_films]

        film_info = {
            'title': details.get('title'),
            'poster': f"https://image.tmdb.org/t/p/original{details.get('poster_path')}",
            'release_date': details.get('release_date'),
            'country': details.get('production_countries', [{}])[0].get('name'),
            'genre': ', '.join([genre['name'] for genre in details.get('genres', [])]),
            'actors': ', '.join(top_cast),
            'age_limit': us_rating,
            'films_to_recommend': films_to_recommend
        }
        return film_info
    return


def search_film(film_title):
    base_url = "https://api.themoviedb.org/3"
    search_url = f"{base_url}/search/movie"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    params = {
        'query': film_title,
        'include_adult': 'true',
        'language': 'en-US',
        'page': 1
    }
    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None


def get_film_details(film_id):
    url = f"https://api.themoviedb.org/3/movie/{film_id}"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def get_film_cast(film_id):
    url = f"https://api.themoviedb.org/3/movie/{film_id}/credits"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def get_film_ratings(film_id):
    url = f"https://api.themoviedb.org/3/movie/{film_id}/release_dates"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def get_similar_films(film_id):
    url = f"https://api.themoviedb.org/3/movie/{film_id}/similar"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

