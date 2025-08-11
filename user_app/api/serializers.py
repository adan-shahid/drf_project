from django.contrib.auth.models import User
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
    #'password2' is the new field we are adding to  User model Manually.
    #'write_only' will hide our password .
    password2 = serializers.CharField(style = {'input_type':'password'} ,write_only = True)
    class Meta:
        model = User
        fields = ['username', 'email' , 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Error": "p1 and p2 should be same."})
        
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({"error":"Email already exists"})