from rest_framework.decorators import api_view
from rest_framework.response import Response
# Import django rest framework request
from rest_framework.request import Request

# Create your views here.
@api_view(['GET'])
def index(request: Request):
    data = request.query_params
    print(data)


    return Response({'result': data})




