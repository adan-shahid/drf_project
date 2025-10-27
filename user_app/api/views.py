from.serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed


def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("user is not active")
    
    refresh = RefreshToken.for_user(user)

    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }

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

            # FOR SIMPLE TOKEN AUTHENTICATION.
            # token = Token.objects.get(user=account).key
            # data['token'] = token

            # FOR SIMPLE JWT TOKEN AUTHENTICATION
            token = get_tokens_for_user(account)
            data['token'] = token

        else:
            data= serializer.errors
        
        return Response(data)
    
#WHEN WE LOGGED OUT, IT SHOULD DELETE THE TOKEN.
@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
        
     

