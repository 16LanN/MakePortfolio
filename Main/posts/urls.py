from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/posts/', PostAPIList.as_view()),
    path('api/v1/post/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v1/postdelete/<int:pk>/', PostAPIDelete.as_view())
]