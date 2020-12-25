from rest_framework import serializers

from stories.models import (
    Recipe,
    Category,
    Tag
)


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


class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

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


class RecipeCreateSerializer(serializers.ModelSerializer):

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
