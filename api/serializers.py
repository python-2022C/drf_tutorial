from .models import Student

from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=5,
    required=True,
    error_messages={
        'required': 'Majburiy',
        'max_length': 'Max 5 ta belgi dan olishi mumkin'
    }
    )
    score = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    