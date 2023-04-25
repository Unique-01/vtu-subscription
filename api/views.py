from django.shortcuts import render
from rest_framework import generics
from .models import MyUser
from .serializers import *
from rest_framework.permissions import *
from rest_framework.authentication import *
from rest_framework.views import APIView

# Create your views here.

class SignUp(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(
            {"message": "Logged out successfully."}, status=status.HTTP_200_OK
        )


