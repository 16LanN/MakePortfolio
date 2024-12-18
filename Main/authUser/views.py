from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema



@extend_schema(
    request=UserSerializer,
    responses={200: UserSerializer},
    tags=['Register']
)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@extend_schema(
    request=UserSerializer,
    responses={200: UserSerializer},
    tags=['Current User update or read']
)
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "nickname": user.nickname,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "id": user.id
        })

    def put(self, request, format=True):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK) 
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)