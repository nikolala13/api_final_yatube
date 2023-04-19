# API YaTube project
## Description
###### API for YaTube social network with standard GET, PUT, POST requests. It is possible to change, receive and add new entries, subscriptions to authors, comments to posts. 

## Tech:
- Django 4.2
- DRF
- JWT + DJOSER

## Running on your PC
- Clone repo:
```sh
git clone https://github.com/nikolala13/api_final_yatube.git
```

- Go to folder with project:
```sh
cd homework_bot
```

- Download venv ( required Python >= 3.7):
```sh
python -m venv venv
```

- Activate venv:
```sh
# OS Lunix & MacOS
source venv/bin/activate
```
```sh
# OS Windows GitBash Terminal
source venv/Scripts/activate
```
```sh
# OS Windows cmd.exe terminal
C:\> venv\Scripts\activate
```

- Install requirements from requirements.txt:
```sh
python3 -m pip install --upgrade pip
```
```sh
pip install -r requirements.txt
```

- Make migrations:
```sh
python manage.py migrate
```
- Create superuser:
```sh
python manage.py createsuperuser
```

- Run project:
```sh
python manage.py runserver
```

## API examples for all users
For unauthorized users, working with the API is available in read mode; it will not be possible to change or create anything.
```sh
GET api/v1/posts/ - get a list of all posts.
When specifying the limit and offset parameters, the output should work with pagination
GET api/v1/posts/{id}/ - getting a post by id
GET api/v1/groups/ - getting a list of available communities
GET api/v1/groups/{id}/ - getting information about the community by id
GET api/v1/{post_id}/comments/ - get all comments on a post
GET api/v1/{post_id}/comments/{id}/ - Getting a comment on a post by id
```
## API examples for authorized users
- To create a post:
```sh
POST /api/v1/posts/
```
body for request:
```sh
{
"text": "string",
"image": "string",
"group": 0
}
```
- Post update:
```sh
PATCH /api/v1/posts/{id}/
```
body for request:
```sh
{
"text": "string",
"image": "string",
"group": 0
}
```
- Partial post update:
 ```sh
POST /api/v1/posts/
```
body for request:
```sh
{
"text": "string",
"image": "string",
"group": 0
}
```
Getting access to the /api/v1/follow/ endpoint (subscriptions) is only available to authorized users.

subscription of the user on whose behalf the request is made to the user passed in the body of the request. Anonymous requests are prohibited.
```sh
GET /api/v1/follow/
```
- Authorized users can create posts, comment on them and follow other users.
- Users can change (delete) the content of which they are the author.

## Getting JWT token:
- Access by an authorized user is available through a JWT token (Joser), which can be obtained by performing a POST request to the address
```sh
POST /api/v1/jwt/create/
```
- Passing user data in body (for example, in postman):
```sh
{
"username": "string",
"password": "string"
}
```
- Add the received token to headers (postman), after which all project functions will be available:
```sh
Authorization: Bearer {your_token}
```
- Update JWT token:
```sh
POST /api/v1/jwt/refresh/
```
- Check JWT token:
```sh
POST /api/v1/jwt/verify/
```
- Also, pagination (LimitOffsetPagination) is implemented in the API project:
```sh
GET /api/v1/posts/?limit=5&offset=0
```