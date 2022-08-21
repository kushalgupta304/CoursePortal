from django.shortcuts import render
from authentication.models import User
from rest_framework.views import APIView
from authentication.serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

# Create your views here.

class Signup(APIView):
    def post(self,request):
        requested_data = request.data
        serialized_data = UserSerializer(data=requested_data)
        if serialized_data.is_valid():
            try:
                data = serialized_data.data
                data.update({"username":data['email']})
                obj = User.objects.create(**data)
                obj.set_password(requested_data.get('password', ""))
                obj.save()
                return Response({"message":"success"})
            except Exception as e:
                return Response({"message":"failure", "error": str(e)}, status=403)
        else:
            return Response({"message":"invalid data", "error":serialized_data.errors})
        
        

class Login(APIView):
    def post(self, request):
        serializer_obj = LoginSerializer(data= request.data)
        if serializer_obj.is_valid():
            try:
                user_obj = User.objects.get(email=serializer_obj.data['email'])
                if check_password(serializer_obj.data['password'], user_obj.password):
                    data = UserSerializer(user_obj).data
                    token= Token.objects.get_or_create(user=user_obj)
                    data.update({"token":token[0].key})
                    return Response({"data":data})
                else:
                    return Response({"message":"failure", "error": "Invalid Creds"}, status=403)

            except User.DoesNotExist:
                return Response({"message":"failure", "error": "Invalid Creds"}, status=403)
        else:
            return Response({"message":"invalid data", "error":serializer_obj.errors}) 