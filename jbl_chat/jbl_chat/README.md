This is a simple chat web-service for Jobylon. Based on user stories:
    1. As a user, I want to be able to see all the other users on the platform.
    2. As a user, I want to be able to see my conversation with another user
    3. As a user, I want to be able to message another user on the platform.

## installation
For this web service we used Django and Django Rest Framework. DRF_YASG was used to build the Swagger documentation.
```sh
    pip install django
    pip install djangorestframework
    pip install drf_yasg
```

## running the app
After installing all the packages above, navigate to you project
```sh
    cd your/path/here
```

Build the sqlite3 of Django
```sh
    python manage.py makemigrations chat
    python manage.py migrate
```

and start the project
```sh
    python manage.py runserver
```

## API documentation
A complete documentation of all endpoints, you can found at http://127.0.0.1:8000/swagger/
But here is some quickly examples of they:
- USERS ENDPOINTS
    GET: http://127.0.0.1:8000/users/
    Will return all users registred

    POST: http://127.0.0.1:8000/users/
    To create a new User to chat
    Body: raw-application/json
    example: 
        {
            "user_firstname":"Jobylon",
            "user_lastname":"Best Company In The World"
        }
    That will return the fields First Name, Last Name and an ID.
    
- CHAT ENDPOINTS
    GET: http://127.0.0.1:8000/chat/
    Will return all messages from all users
    
    GET: http://http://127.0.0.1:8000/chat/{from_id}&{to_id}
    If you inform two User IDs of reference, that will return all the messages from the chat of these users.
    For example: http://127.0.0.1:8000/chat/?from_id=1&to_id=2 will return:
[
    {
        "id": 1,
        "message": "Hello",
        "from_id": 1,
        "to_id": 2
    },
    {
        "id": 2,
        "message": "Hello, everything is ok?",
        "from_id": 2,
        "to_id": 1
    },
    {
        "id": 3,
        "message": "I'm really fine, and you?",
        "from_id": 1,
        "to_id": 2
    },
    {
        "id": 4,
        "message": "Great",
        "from_id": 2,
        "to_id": 1
    },
    {
        "id": 6,
        "message": "Are you there?",
        "from_id": 1,
        "to_id": 2
    }
]

    POST: http://127.0.0.1:8000/chat/
    To send a new message to any user
    Body: raw-application/json
    example: 
        {
        	"from_id":1,
        	"to_id":2,
            "message":"Hey, I'm testing the new chat"
        }
    Will return the fields from_id, to_id and the message itself.
    
## USERS
A simple test user was created
Username: jobylontest
Password: jobtest1234

For admin access, please contact me at luiz.gustavo.silva1@outlook.com or +55 11 949456636
    