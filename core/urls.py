
from django.contrib import admin
from django.urls import path
from api.views import index,addStudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('addStudent/',addStudent)

]
