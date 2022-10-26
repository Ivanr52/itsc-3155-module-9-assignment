from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    name = request.form.get('name')
    director = request.form.get('director')
    rating = request.form.get('rating')
    movie_repository.create_movie(name, director, rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    searched_title = request.args.get('searched')   
    if searched_title is None:
        found_movie = None
    else:
        found_movie = movie_repository.get_movie_by_title(searched_title)
        if found_movie is None:
            found_movie = 'Not Found'
    return render_template('search_movies.html', search_active=True, found_movie=found_movie)
