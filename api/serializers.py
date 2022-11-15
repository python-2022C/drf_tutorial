from .models import Student

from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    score = serializers.IntegerField()
    city = serializers.CharField(max_length=50)


    