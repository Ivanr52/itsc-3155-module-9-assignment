# TODO: Feature 2
from app import app
from src.repositories.movie_repository import get_movie_repository


def test_create_movie():
    # Create a movie
    get_movie_repository().create_movie('John Wick', 'Chad Stahelski', 4)
    # Get all movies
    get_movie = get_movie_repository().get_all_movies()
    # There should be 2 movies, The one created above, and one created in the test_create_movies_page.py
    assert len(get_movie) == 5 # 3 movies created in e2e/test_all_movies_pages.py
    # Assert the movie title is the one from above
    assert get_movie_repository().get_movie_by_title('John Wick')
