# TODO: Feature 1
from src.repositories import movie_repository as movie_r
from app import app

def test_list_all_movies_page_rating_bounds():
    movie_repository = movie_r.get_movie_repository()
    movie_repository.create_movie("Title1", "director1", -1)
    movie_repository.create_movie("Title2", "director2", 0)
    movie_repository.create_movie("Title3", "director3", 3)
    movie_repository.create_movie("Title4", "director4", 6)
    for movie in movie_repository.get_all_movies():
        assert movie.rating >= 0
        assert movie.rating <= 5



