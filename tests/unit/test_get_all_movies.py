# TODO: Feature 1
# TODO: Feature 1
from src.repositories import movie_repository as movie_r
from app import app
def test_list_all_movies_page():
    test_app = app.test_client()
    movie_repository = movie_r.get_movie_repository()
    movie_repository.create_movie("Title1", "director1", 3)
    movie_repository.create_movie("Title2", "director2", 0)
    movie_repository.create_movie("Title3", "director3", 5)
    response = test_app.get('/movies')
    assert b'<td>Title1</td>' in response.data
    assert b'<td>Title2</td>' in response.data
    assert b'<td>Title3</td>' in response.data
    assert b'<td>director1</td>' in response.data
    assert b'<td>director2</td>' in response.data
    assert b'<td>director3</td>' in response.data

def test_list_all_movies_page_rating_bounds():
    movie_repository = movie_r.get_movie_repository()
    movie_repository.create_movie("Title1", "director1", -1)
    movie_repository.create_movie("Title2", "director2", 0)
    movie_repository.create_movie("Title3", "director3", 3)
    movie_repository.create_movie("Title4", "director4", 6)
    for movie in movie_repository.get_all_movies():
        assert movie.rating >= 0
        assert movie.rating <= 5



