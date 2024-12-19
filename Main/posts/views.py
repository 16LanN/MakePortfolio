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
        tags=['Users posts']
    )
class UserPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user_id__id=user_id)


@extend_schema(
        request={},
        responses={201: PostSerializer},
        tags=['Own posts']
    )
class CurrentUserPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user)






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

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

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