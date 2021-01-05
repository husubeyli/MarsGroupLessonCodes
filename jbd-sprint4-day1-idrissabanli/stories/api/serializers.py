from rest_framework import serializers
from django.contrib.auth import get_user_model

from stories.models import (
    Recipe,
    Category,
    Tag, RecipeComment
)

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
            'created_at'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title'
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeComment
        fields = (
            'user',
            'text',
        )


class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'short_description',
            'tags',
            'comments',
            'owner',
            'category',
            'slug',
            'image',
            'created_at',
        )

    def get_comments(self, recipe):
        return CommentSerializer(recipe.comments.all(), many=True).data


class RecipeCreateSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True), required=False)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'short_description',
            'tags',
            'owner',
            'category',
            'slug',
            'image',
            'created_at',
        )

    def validate(self, attrs):
        request = self.context.get('request')
        owner = request.user
        attrs['owner'] = owner
        return attrs
