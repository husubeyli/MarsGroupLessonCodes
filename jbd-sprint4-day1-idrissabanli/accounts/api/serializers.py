from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'image',
            'bio',
            'date_joined',
            'last_login',
            'token'
        )

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password,])

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'image',
            'bio',
            'date_joined',
            'last_login',
        )
        
    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        user.save()
        return user
