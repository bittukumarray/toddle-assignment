from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class Signup(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            user=User.objects.create(username=username)
            user.set_password(password)
            user.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),'access': str(refresh.access_token),})
        except:
            return Response({"msg":"This username already exists in the database"}, status=status.HTTP_400_BAD_REQUEST)


