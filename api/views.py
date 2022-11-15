from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def index(request):
    data = request.data
    print(type(data))
    print(data)
    return Response({'message': 'Hello, World!'})


def home(request):
    data = request.body
    print(type(data))
    print(data)
    return JsonResponse({'message': 'Hello, World!'})


