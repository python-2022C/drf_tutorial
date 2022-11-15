from rest_framework.decorators import api_view
from rest_framework.response import Response
# Import django rest framework request
from rest_framework.request import Request
from .models import Student
# Create your views here.
@api_view(['GET'])
def index(request: Request):
    data = request.query_params
    print(data)


    return Response({'result': data})


@api_view(['POST'])
def addStudent(request: Request):
    data = request.data
    name = data.get('name','Ali')
    score = data.get('score',0)
    city = data.get('city','Jizzax')

    student = Student(name=name,score=score,city=city)
    student.save()   

    
    return Response({'result': data})



