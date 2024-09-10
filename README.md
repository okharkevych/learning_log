# learning_log

Learning Log web app (built with django and bootstrap) helps users record and 
review materials being learned in the 'topic-entry' format.

Entries can be edited after creation. Entries are
associated with a particular topic and can only be accessed within this topic.
Topics are available only to their creators. For now, there are no materials
available to unauthenticated users.

Therefore, website requires visitors to register/log in to be able to review or
create their topics/entries.

Logout functionality, as well as admin user are also implemented.

Last but not least, the web app has customized error handling for common errors.

Learning Log is ready for deployment on https://www.heroku.com/

Please note that 'heroku-postgresql' (aka Heroku Postgres) addon is required on
the side of Heroku for PostgreSQL database to work.

<div align=center margin=auto> 
  <img src="images/home_page.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/registration.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/login.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/logged_out.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/topics.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/topic_1.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/topic_2.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/edit_entry.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/add_topic.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/add_entry.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/404.png" width=80%>
</div>

<div align=center margin=auto> 
  <img src="images/505.png" width=80%>
</div>


## Table of Contents
1. [Prerequisites](README.md#prerequisites)
2. [Installation on Linux](README.md#installation-on-linux)
    * [Standard dependencies](README.md#standard-dependencies)
    * [Repository import](README.md#repository-import)
    * [Project-specific dependencies](README.md#project-specific-dependencies)
3. [How to run locally](README.md#how-to-run-locally)


## Prerequisites
To run the app locally, you need the following components installed:

**Standard dependencies**
- Python 3.10
- Pip
- Git
- Pipenv (highly-recommended in this case, to avoid installing specific 
dependency versions required by the app system-wide; instead, dependecies 
are installed within a virtual environment dedicated to the app, and the 
environment ensures expected behavior of the app; also, automates dependency 
installation) 

**Project-specific dependencies**
- django (web framework for website development)
- django-bootstrap4 (bootstrap framework integration to create user interface)
- python-dotenv (to work with environment variables)
- psycopg2 (to use database on Heroku side)
- django-heroku (to configure web app for running on Heroku server)
- gunicorn (server providing access to web apps on Heroku server)


## Installation on Linux

### Standard dependencies
Please refer to the corresponding official sources for:
- Python: https://www.python.org/downloads/
- Pip: https://pip.pypa.io/en/stable/installation/
- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- Pipenv: https://pipenv.pypa.io/en/latest/

### Repository import
- Go to the directory you'd like to have this repository in and open the 
directory in terminal
- Enter the following command:

```
>>> git clone https://github.com/okharkevych/learning_log.git
```

### Project-specific dependencies
- Open learning_log directory downloaded earlier in terminal
- Enter the following commands:

```
>>> pipenv shell
>>> pipenv install
```


## How to run locally
- Open learning_log directory downloaded earlier in terminal
- Enter the following command:

```
>>> pipenv shell
>>> python manage.py migrate
>>> python manage.py runserver
```

- Terminal output will contain a line like 
"Starting development server at http://127.0.0.1:8000/"
- Open the link from the terminal in your browser
- Enjoy the app!