from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[EmailValidator(message="Invalid email format")]
    )
    password = serializers.CharField(
        write_only=True,
        required=False,
        validators=[validate_password],
        min_length=8,
        error_messages={
            "min_length": "Password must be at least 8 characters long"
        }
    )
    confirm_password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = get_user_model()
        fields = ['nickname', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'nickname': {'required': True, 'min_length': 4, 'error_messages': {
                "min_length": "Username must be at least 4 characters long"
            }},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise serializers.ValidationError({"confirm_password": "Passwords do not match"})
        elif password or confirm_password:
            raise serializers.ValidationError({"confirm_password": "Both password fields are required"})

        return attrs
    
    def update(self, instance, validated_data):
        validated_data.pop('confirm_password', None)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(
            nickname=validated_data['nickname'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user