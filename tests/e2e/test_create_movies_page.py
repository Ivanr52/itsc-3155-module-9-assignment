# TODO: Feature 2
from app import app


def test_create_movies_page():
    test_app = app.test_client()
    response = test_app.get('/movies/new')
    assert b'<p class="mb-3">Create a movie rating below</p>' in response.data


def test_create_movies_page_with_info():
    test_app = app.test_client()
    response = test_app.post('/movies', data={
        'name': 'Star Wars',
        'director': 'George Lucas',
        'rating': 5,
    }, follow_redirects=True)
    assert response.status_code == 200
