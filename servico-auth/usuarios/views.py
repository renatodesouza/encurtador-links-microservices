from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import UserRegisterSerializer

@api_view(['GET'])
def health_check(request):
    """
    Retorna 200 OK se o serviço estiver no ar.
    """
    return Response(
        {"message": "Serviço de Autenticação está no ar!"}, 
        status=status.HTTP_200_OK
    )

# Nova view registro de usuário
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    # Não precisa de autenticação para registra
    permission_classes = []


