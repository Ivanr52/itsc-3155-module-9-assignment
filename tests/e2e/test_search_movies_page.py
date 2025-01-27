# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import app

def test_search_movies():
    test_app = app.test_client()
    response = test_app.get('/movies/search')
    assert b'<p class="mb-3">Search for a movie rating below</p>' in response.data

def test_search_movies_with_movie():
    test_app = app.test_client()
    response = test_app.get('/movies/search?searched=Star+Wars')
    assert b'<h2 class="text-center">Found your movie!</h2>' in response.data
    assert b'<th>Star Wars</th>' in response.data

def test_search_movies_with_wrong_movie():
    test_app = app.test_client()
    response = test_app.get('/movies/search?searched=Startrek')
    assert b'<h2 class="text-center">Could not find your movie</h2>' in response.data