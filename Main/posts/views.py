from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import *
from .permissions import *
from drf_spectacular.utils import extend_schema
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

@extend_schema(
        request={},
        responses={201: PostSerializer},
        tags=['All posts and create']
    )
class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

@extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer},
        tags=['Detail Post']
    )
class PostAPIDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnlyOrOnlyOwner, )

@extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer},
        tags=['Filter']
    )
class FilteredPostAPIList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PostFilter
    ordering_fields = ['date', 'title']
    ordering = ['date']