from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/posts/', PostAPIList.as_view(), name='posts'),
    path('api/v1/posts/<int:pk>/', PostAPIDelete.as_view(), name='post_detail'),
    path('api/v1/posts/filtered/', FilteredPostAPIList.as_view(), name='filtered_posts'),

    path('api/v1/users/<int:user_id>/posts/', UserPostsListView.as_view(), name='user-posts'),
    path('api/v1/my/posts/', CurrentUserPostsListView.as_view(), name='current-user-posts'),
]