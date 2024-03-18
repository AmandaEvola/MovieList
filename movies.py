# import necessary packages
from flask import Flask, jsonify, request
import requests

# create Flask app
app = Flask(__name__)

# TMDb API key
API_KEY = '34e71e9b906a4c80db7d91bf64ed4b02'
BASE_URL = 'https://api.themoviedb.org/3'

# Function to search for movies using TMDb API
def search_movies(query):
    url = f'{BASE_URL}/search/movie'
    params = {'api_key': API_KEY, 'query': query}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []

# define the API routes
@app.route('/')
def index():
    # return a list of movies
    movies = [
        {'title': 'The Dark Knight', 'year': 2008, 'duration': 152},
        {'title': 'The Godfather', 'year': 1972, 'duration': 178},
        {'title': 'Toy Story', 'year': 1995, 'duration': 92}
    ]
    return jsonify(movies)

# Route to search for movies
@app.route('/search')
def search():
    query = request.args.get('query')
    if query:
        movies = search_movies(query)
        return jsonify({'movies': movies})
    else:
        return 'No query provided'

# run the app
if __name__ == '__main__':
    app.run(debug=True)
