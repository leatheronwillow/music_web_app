
# Music Web App Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Home route
GET /home

# Waving route
GET /wave?name=

# Submit message route
POST /submit
  name: string
  message: string

POST /albums
  title=Voyage
  release_year=2022
  artist_id=2
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# POST /albums
#  Parameters: 
#    title: Voyage
#    release_year: 2022
#    artist_id: 2
#  Expected response (200 Ok):
"""
None
"""

# POST /albums
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide details of an album
"""

# GET /albums
#  Expected response (200 OK):
"""
returns list of albums which includes the newly added album
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

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
    response = web_client.post('/albums', album={'title':'Voyage', 'release_year': '2022', 'artist_id': 2})
    assert response.status_code == 200
    response.data.decode('utf-8') == 'Album added successfully'
    response = web_client.get('/albums')
    assert response.data.decode('utf-8') == 'Doolittle, Surfer Rosa, Waterloo, Voyage'

"""
POST /albums
 Parameters: none
 Expected response (400 Bad Request): 'Album Details not found'
"""


'''