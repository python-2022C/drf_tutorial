# Django rest framework tutorial

## 1. Create a new project

```bash
django-admin startproject tutorial
```

## 2. Create a new app

```bash
python manage.py startapp quickstart
```

## 3. Add the app to the project

```python
# tutorial/settings.py
INSTALLED_APPS = [
    ...
    'quickstart',
]
```

## 4. Create a view

```python
# quickstart/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

