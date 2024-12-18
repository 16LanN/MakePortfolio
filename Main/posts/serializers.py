from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('title', 'description', 'date', "user_id")
        read_only_fields = ['user_id']