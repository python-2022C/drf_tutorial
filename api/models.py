from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default='Jizzax',blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

