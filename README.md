# Flask-JWT-Auth
Flask JWT based authorization server script template.


## Getting started

1. Pull and get into the repo
```bash
git clone https://github.com/geeksloth/Flask-JWT-Auth.git && cd Flask-JWT-Auth
```


2. Install requirements and add submodule
```bash
python -m pip install --upgrade pip
pip install Flask Flask-JWT PyJWT Werkzeug
git submodule add https://github.com/geeksloth/gslothutils
```

3. Usage
- Run the scrip:
```bash
python api.py
```

- Request an access token (or use *PostMan* to make the request in more practical way)
```bash
curl -d '{"username": "user1","password": "password1" }' -H "Content-Type: application/json" -X POST http://localhost:5005/auth
```
You will get the ```access_token``` eg. ```eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjkwMjI2OTEsImlhdCI6MTY2OTAyMjM5MSwibmJmIjoxNjY5MDIyMzkxLCJpZGVudGl0eSI6MX0.JdiTA9t_U-266mq-gTiAbwRmS2f87x6RRYg2gKqMIt4```

- Use ```access_token``` to access the authorized function
```bash
curl -H "Authorization: JWT <access_token>" http://localhost:5005/hi
```
You will get the response from server ie. ```Hi, Client(id=1)```


## Optional Recommendations
- You better to use *PostMan* software to make a request in more easier way.
- In the request's headers, add **Authorization** key with ```JWT <access_token>``` value, available to both POST and GET methods.
