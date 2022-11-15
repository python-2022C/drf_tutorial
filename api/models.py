from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    city = models.CharField(max_length=50, default='Jizzax',blank=True)

    def __str__(self):
        return self.name