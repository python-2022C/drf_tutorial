from .models import Student,Course

from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50,
    required=True,
   
    )
    score = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    
 

    

    def create(self, validated_data):
        return Student.objects.create(**validated_data)  #         
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.score = validated_data.get('score', instance.score)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


    