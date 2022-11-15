# Django rest framework tutorial

## 1. Create a new project

```bash
django-admin startproject core .
```

## 2. Create a new app

```bash
python manage.py startapp api
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

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})

```

## 5. Create a URL

```python
# quickstart/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('index', index),
]
```