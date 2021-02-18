# Company-Service-Task-

### Project Structure
```
│   db.sqlite3
│   manage.py
│   README.md
│   requirements.txt
│
├───serviceApp
│   │   admin.py
│   │   apps.py
│   │   forms.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-38.pyc
│   │           __init__.cpython-38.pyc
│   │
│   ├───templates
│   │       base.html
│   │       lead.html
│   │       screen2.html
│   │       screen3.html
│   │
│   └───__pycache__
│           admin.cpython-38.pyc
│           models.cpython-38.pyc
│           urls.cpython-38.pyc
│           views.cpython-38.pyc
│           __init__.cpython-38.pyc
│
└───ServiceProject
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
    │
    └───__pycache__
            settings.cpython-38.pyc
            urls.cpython-38.pyc
            wsgi.cpython-38.pyc
            __init__.cpython-38.pyc

```


## Getting Started
### Pre-requisites and Local Development Server
* run pip install -r requirements.txt to install all packages and libraries needed for the project  
* navigate to the project
     *run python manage.py makemigrations 
     * run python manage.py migrate 
     * run python manage.py runserver 
  
  ## The application is run at http://127.0.0.1:8000/lead/
  
