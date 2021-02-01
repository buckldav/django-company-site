# django-company-site
For AP Computer Science Principles class

## Setup
VSCode Extenstions: 
* ```hediet.vscode-drawio```
* ```ms-python.python```
* ```batisteo.vscode-django```
See ```.vscode/settings.json``` for custom editor settings.

Terminal stuff:
```bash
# Create a virtual environment.
python3 -m venv env
# Activate your virtual environment. All python packages will stored in env.
source env/bin/activate
# Install the requisite python packages (and their dependencies) in your virtual environment.
pip install Django Pillow python-dotenv
# Record what you installed with pip in a requirements.txt file.
pip freeze > requirements.txt
# Create a django project folder
# The . is for the current directory
# The company is the project/folder name
django-admin startproject company . 
# Generate SECRET_KEY into a .dotenv
python3 -c "import secrets; print(f'SECRET_KEY={secrets.token_urlsafe()}')" > .env
```

Edit ```company/settings.py```:
```python
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
```

Add .gitignore file with the following. We do not want to publicize our SECRET_KEY in the .env or put our database on GitHub!
```
.env
env
__pycache__
*.sqlite3*
```

Run your server (terminal)
```bash
python3 manage.py runserver
```