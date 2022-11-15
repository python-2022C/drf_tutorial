from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
    data = request.data
    print(type(data))
    print(data)
    return Response({'message': 'Hello, World!'})



