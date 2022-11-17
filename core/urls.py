
from django.contrib import admin
from django.urls import path
from api.views import(
    index,
    addStudent,
    getStudents,
    getStudent,
    removeStudent,
    getCourses
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('addStudent/',addStudent),
    path('getStudent/',getStudents),
    path('getStudent/<int:id>/',getStudent),
    path('getStudent/<int:id>/remove',removeStudent),
    path('getCourses/',getCourses),

]
