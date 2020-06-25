"users": "http://127.0.0.1:8000/api/users/", - CRUD users, Only user can update himself
        {
        "id": 2,
        "username": "Ulfric",
        "last_name": "",
        "first_name": ""
    }

"posts": "http://127.0.0.1:8000/api/posts/", - CRUD posts, Only author can update post
       {
        "id": 2,
        "author": 2,
        "author_name": "Ulfric",
        "title": "Street-Fighting Mathematics",
        "link": "https://www.google.com.ua/Street-Fighting Mathematics",
        "amount_of_upvotes": 2,
        "created": "2020-06-25T15:39:04.175574Z"
    },

"comments": "http://127.0.0.1:8000/api/comments/" - CRUD comments, Only author can update post
        {
        "id": 1,
        "post": {
            "id": 1,
            "author": 1,
            "author_name": "pavlo",
            "title": "Symbian Won",
            "link": "https://www.google.com.ua/",
            "amount_of_upvotes": 1,
            "created": "2020-06-25T15:10:37.461063Z"
        },
        "author": 1,
        "author_name": "pavlo",
        "content": "Somethink",
        "created": "2020-06-25T15:14:51.976408Z"
    }

"add_upvote": "http://127.0.0.1:8000/api/posts/<int:id>/add_upvote" - Use to create upvote by authorized user


content/management/commands/restart_upvotes.py - Use to clean post upvotes
You can easy use crontab for task:
0 1 * * * /path/to/virtualenv/bin/python /path/to/project/manage.py add_upvote