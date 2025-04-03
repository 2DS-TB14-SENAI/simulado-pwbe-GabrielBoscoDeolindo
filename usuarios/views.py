from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    telefone = request.data.get('telefone')
    
    if not username or not password or not telefone:
        return Response({'erro': 'Informações insuficientes'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(username = username).exists():
        return Response({"erro": "user já existe"}, status=status.HTTP_400_BAD_REQUEST)

    usuario = Usuario.objects.create_user(
        username=username,
        password=password,
        telefone=telefone,
    )
    return Response({"Mensagem": f"usuario {username} criado com sucesso"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    telefone = request.data.get('telefone')

    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'acess':str(refresh.access_token),
            'refresh':str(refresh),
        }, status.HTTP_200_OK)
    else:
        return Response({"Erro": "usuário ou senha invalidos"}, status=status.HTTP_401_UNAUTHORIZED)

