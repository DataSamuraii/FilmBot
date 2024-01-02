import requests
import os
from dotenv import load_dotenv

load_dotenv()
TMDb_API_KEY = os.getenv('TMDb_API_KEY')


def get_movie_from_search(movie_title):
    search_results = search_movie(movie_title)
    if not search_results:
        return []

    movie = search_results.get('results', [])[0]
    details = get_movie_details(movie['id'])
    if details:
        movie_cast = get_movie_cast(movie['id'])
        top_cast = [cast_member['name'] for cast_member in movie_cast.get('cast', [])[:5]]

        movie_ratings = get_movie_ratings(movie['id'])
        us_rating = next((rating['certification'] for country_ratings in movie_ratings.get('results', [])
                          for rating in country_ratings['release_dates']
                          if country_ratings['iso_3166_1'] == 'US'), 'NR')

        similar_movies = get_similar_movies(movie['id']).get('results')[:5]
        movies_to_recommend = [movie.get('title') for movie in similar_movies]

        movie_info = {
            'title': details.get('title'),
            'poster': f"https://image.tmdb.org/t/p/original{details.get('poster_path')}",
            'release_date': details.get('release_date'),
            'country': details.get('production_countries', [{}])[0].get('name'),
            'genre': ', '.join([genre['name'] for genre in details.get('genres', [])]),
            'actors': ', '.join(top_cast),
            'age_limit': us_rating,
            'movies_to_recommend': movies_to_recommend
        }
        return movie_info
    return


def search_movie(movie_title):
    base_url = "https://api.themoviedb.org/3"
    search_url = f"{base_url}/search/movie"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    params = {
        'query': movie_title,
        'include_adult': 'false',
        'language': 'en-US',
        'page': 1
    }
    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None


def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def get_movie_cast(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def get_movie_ratings(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None


def get_similar_movies(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar"
    headers = {
        'accept': 'application/json',
        "Authorization": TMDb_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

