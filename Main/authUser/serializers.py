from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['nickname', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)