from .models import Student

from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50,
    required=True,
   
    )
    score = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(
            name=validated_data['name'],
            score=validated_data['score'],
            city=validated_data['city']            
        )

    