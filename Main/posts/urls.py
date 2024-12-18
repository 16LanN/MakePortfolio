from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/posts/', PostAPIList.as_view(), name='posts'),
    path('api/v1/posts/<int:pk>/', PostAPIDelete.as_view(), name='post_detail')
]