from .serializers import userSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class userAV(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = userSerializer(user, many=True)
        return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = watchListSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)