from rest_framework.decorators import api_view
from rest_framework.response import Response
# Import django rest framework request
from rest_framework.request import Request
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
@api_view(['GET'])
def index(request: Request):
    data = request.query_params
    print(data)


    return Response({'result': data})


@api_view(['POST'])
def addStudent(request: Request):
    data = request.data
    print(data)


    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'result': 'Student added successfully'})
    else:
        return Response({'result': 'Error'})
    # print(serializer.is_valid())



     

    




