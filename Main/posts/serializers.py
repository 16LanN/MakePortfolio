from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('title', 'description', 'date', 'user')