from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# from tutorial.quickstart.serializers import UserSerializer

from users.serializers import RegisterSerializer, UserSerializer


# Create your views here.

class RegisterView(APIView):
    """  Handle user registration. """

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """ Handle user login and return JWT token pair. """

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class CustomLogin(LoginView):
    template_name = 'users/custom_login.html'
