from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date', "user_id", 'image')
        read_only_fields = ['id', 'user_id']