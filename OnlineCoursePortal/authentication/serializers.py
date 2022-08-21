from rest_framework import serializers
from authentication.models import User

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=100)
    last_name = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True, max_length=200)
    user_type = serializers.CharField(required=True, max_length=20)

    class Meta:
        field = ('first_name', 'last_name', 'email', 'user_type')



class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True, max_length=200)
    password = serializers.CharField(required=True, max_length=100)

    class Meta:
        field = ('email', 'password')