# Django project

### Initial setup

Make a directory and install django through pipenv

```
mkdir projectname && cd projectname
mkdir src && cd src
pipenv install django==1.11.17 --python 3.7
```

Make sure you have boto3 install using pip freeze
```
pipenv shell

pip freeze
```

Start a new django project, then make a settings directory and cd into it.
```
django-admin startproject projecthome .
cd projecthome
mkdir settings && cd settings
```

Make a file called __init__.py and drop this code in it:
```python
from .base import *

from .production import *

try:
  from .local import *
except:
  pass
```

Open settings.py and change the base directory to this (one level down):

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

Move settings.py to settings/ directory and rename base.py. Make copies of base.py to local.py and production.py
```
mv settings.py settings/base.py
cd settings
cp base.py local.py
cp base.py local.py
```

Navigate back to the root of the project (where manage.py is) and run python manage.py migrate. Also create a superuser
```
python manage.py migrate

python manage.py createsuperuser
```










