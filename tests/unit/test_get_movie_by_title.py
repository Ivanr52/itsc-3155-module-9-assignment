# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
from app import app

def test_get_movie_by_title():

    movie = get_movie_repository().create_movie('Star Wars', 'George Lucas', 5)
    get_movie = get_movie_repository().get_movie_by_title('Star Wars')
    none_movie = get_movie_repository().get_movie_by_title('Startrek')

    assert type(get_movie) == Movie
    assert get_movie.title == 'Star Wars'
    assert none_movie is None
