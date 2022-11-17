from rest_framework.decorators import api_view
from rest_framework.response import Response
# Import django rest framework request
from rest_framework.request import Request
from .models import Student,Course
from .serializers import StudentSerializer,CourseSerializer
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
        return Response(serializer.errors)
    # print(serializer.is_valid())


@api_view(['GET'])
def getStudents(request: Request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def getStudent(request: Request, id):
    # Check if student exists
    try:
        students = Student.objects.get(id=id)
        serializer = StudentSerializer(students)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({'result': 'Student not found'})
    

@api_view(['GET'])
def removeStudent(request: Request, id):
    students = Student.objects.get(id=id)
    students.delete()
    return Response({'result': 'Student removed successfully'})



     
@api_view(['GET'])
def getCourses(request: Request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
    




