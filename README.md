"users": "http://127.0.0.1:8000/api/users/", - CRUD users, Only user can update himself

"posts": "http://127.0.0.1:8000/api/posts/", - CRUD posts, Only author can update post

"comments": "http://127.0.0.1:8000/api/comments/" - CRUD comments, Only author can update post

"add_upvote": "http://127.0.0.1:8000/api/posts/<int:id>/add_upvote" - Use to create upvote by authorized user


content/management/commands/restart_upvotes.py - Use to clean post upvotes
You can easy use crontab for task:
0 1 * * * /path/to/virtualenv/bin/python /path/to/project/manage.py add_upvote