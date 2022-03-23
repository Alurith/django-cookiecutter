# Django cookiecutter template  
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for [Django](https://www.djangoproject.com/) using [Postgres](https://www.postgresql.org/), [htmx ](https://htmx.org/) and [Tailwindcss ](https://tailwindcss.com/).

## The Stack:
| PACKAGE     | VERSION |
| ----------- | ------- |
| Python      | 3.8     |
| Django      | 4.0.3   |
| Postgres    | latest  |
| htmx        | 1.7.0   |
| Tailwindcss | 3.0     |

## How to use
Install the latest Cookiecutter:
```
pip install cookiecutter
```
Generate a new Project:
```
cookiecutter https://github.com/Alurith/django-cookiecutter.git
```
Create the .env file (update with your own values):
```
# postgres variables for docker
POSTGRES_DB = database_name
POSTGRES_USER = user
POSTGRES_PASSWORD = password
POSTGRES_ROOT_PASSWORD = rootpassword

# database url for dj-database-url
DATABASE_URL = postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

# DJANGO
DEBUG = True
```
Run the project with docker:
```
docker-compose up 
```
Now you're ready!
 
## Update Philosophy
TBD
## Issues & Pull Request
Please describe your issue as clear as possible, so I can replicate the problem. Also, if you already worked on a fix you can submit a pull request.
