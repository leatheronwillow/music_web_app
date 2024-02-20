# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

"""
GET /albums
Expected response (200 OK):
Returns list of album titles
"""
def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Doolittle, Surfer Rosa, Waterloo'

"""
POST /albums
 Parameters: 
   title: Voyage
   release_year: 2022
   artist_id: 2
 Expected response (200 Ok): 
   returns None
   running GET /albums returns 'Doolittle, Surfer Rosa, Voyage' 
"""
def test_post_albums(web_client):
    response = web_client.post('/albums', data={'title':'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Album added successfully'
    response = web_client.get('/albums')
    assert response.data.decode('utf-8') == 'Doolittle, Surfer Rosa, Waterloo, Voyage'