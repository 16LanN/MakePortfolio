from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import *
from .permissions import *
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

@extend_schema(
        request={},
        responses={201: PostSerializer},
        tags=['Posts']
    )
class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

@extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer},
        tags=['Posts']
    )
class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )

@extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer},
        tags=['Posts']
    )
class PostAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnlyOrOnlyOwner, )

