from django.urls import path, include
from .views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('current/', CurrentUserView.as_view(), name='current'),
    path('all-users', AllUsersView.as_view(), name='all-users')
]