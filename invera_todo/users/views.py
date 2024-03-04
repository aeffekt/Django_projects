from rest_framework import viewsets, views
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import logout

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth import authenticate


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(views.APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # Your authentication logic here
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            user_serialized = UserSerializer(user)
            return Response({'token': token.key, 'user': user_serialized.data})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
    

class LogoutView(views.APIView):
    def get(self, request):        
        logout(request)
        return Response({'message': 'Logout exitoso'})