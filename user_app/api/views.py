from.serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST',])
def registerUser(request):
    if request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      
     

