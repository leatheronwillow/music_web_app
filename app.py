import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repo import AlbumRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    album_titles = []
    for album in albums:
        title = album.title
        album_titles.append(title)
    return ', '.join(album_titles)

@app.route('/albums', methods=['POST'])
def post_albums():
    form = request.form
    if 'title' not in form or 'release_year' not in form or 'artist_id' not in form:
        return 'Album Details not found', 400 
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.create(Album(None, request.form['title'], request.form['release_year'], request.form['artist_id']))
    return 'Album added successfully'

    


# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

