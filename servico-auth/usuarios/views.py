from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def health_check(request):
    """
    Retorna 200 OK se o serviço estiver no ar.
    """
    return Response(
        {"message": "Serviço de Autenticação está no ar!"}, 
        status=status.HTTP_200_OK
    )

# Create your views here.
