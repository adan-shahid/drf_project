from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                UserSerializer(user).data,
                status= status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = refresh_token(refresh_token)
            token.backlist()
            return Response('Logged out Successfully')
        except KeyError:
            return Response('Refresh Token Required', status = status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response('Invalid/Expired Token', status= status.HTTP_400_BAD_REQUEST)
        
         
        
         



class ProfileView(APIView):
    pass 