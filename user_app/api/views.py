from.serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token



@api_view(['POST',])
def registerUser(request):
    if request.method == 'POST':
        serializer = userSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful."
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data= serializer.errors
        
        return Response(data)
      
     

