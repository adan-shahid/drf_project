from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length = 8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
        read_only_fields = ['id']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match.')
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        self.password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(self.password)
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'full_name', 'created_at']
        read_only_fields = ['id', 'created_at']