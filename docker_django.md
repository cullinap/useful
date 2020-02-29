# Use django in docker

### basic setup

Make a directory cd into it and install django through pipenv

```
mkdir simple_dj_docker && cd simple_dj_docker
pipenv install django==2.2.4 gunicorn --python 3.7
```

Activate pipenv shell and check the install and files inside the project

```
pipenv shell
pip freeze
ls
```

Create your django project, run migrations, and make superuser
```
django-admin startproject projecthome .
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Open projecthome/settings.py
```
open projecthome/settings.py
```

Post the following code to replace the DEBUG settings in the settings.py file
```python
DEBUG = int(os.environ.get('DEBUG', default=1))
```

Create a .env file
```
nano .env
```

Paste in `DEBUG=1`

Press CTRL X and then Y ENTER to save and exit the file.

Test Gunicorn
```
gunicorn projecthome.wsgi:application --bind 0.0.0.0:8000
```

Go to localhost:8000 to see the beginning of the project.

Use CTRL C to exit from gunicorn.

### Make dockerfile

Make the dockerfile and open it up in your favorite editor

```
touch Dockerfile
subl .
```

Post the following code into the Dockerfile

```
# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev

EXPOSE 8000
CMD gunicorn projecthome.wsgi:application --bind 0.0.0.0:$PORT
```

Build the docker image
```
docker build -t simple-dj-docker -f Dockerfile .
```

Run the container after it builds

```
docker run -it -p 80:8000 simple-dj-docker
```

Shut down docker if you need to: CTRL C

Run the container in the background
```
docker run -it -d -p 80:8000 simple-dj-docker
```

Shut down the container. 1) find the id from docker ps 2) run docker stop
```
docker ps

docker stop <container-id>
```

Exit pipenv: CTRL D










