from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from stories.api.serializers import (
    RecipeSerializer,
    RecipeCreateSerializer
)
from stories.models import (
    Recipe,
)


class RecipeAPIView(APIView):
    model = Recipe

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.filter(is_published=True)
        serializer = RecipeSerializer(recipes, many=True, context={'request': request})
        print(serializer.data)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        recipe_data = request.data
        serializer = RecipeCreateSerializer(data=recipe_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        d = serializer.data
        d.update({'message': 'success'})
        return Response(data=d, status=HTTP_201_CREATED)


class RecipeRetrieveUpdateDeleteAPIView(APIView):

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        recipe = Recipe.objects.filter(slug=slug, is_published=True).first()
        if not recipe:
            raise NotFound({'message': 'recipe not found', 'detail': 'Not found'})
        serializer = RecipeSerializer(recipe, context={'request': request})
        print(serializer.data)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        recipe_data = request.data
        recipe = Recipe.objects.filter(slug=slug, is_published=True).first()
        if not recipe:
            raise NotFound({'message': 'recipe not found', 'detail': 'Not found'})
        serializer = RecipeCreateSerializer(data=recipe_data, instance=recipe, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        recipe_data = request.data
        recipe = Recipe.objects.filter(slug=slug, is_published=True).first()
        if not recipe:
            raise NotFound({'message': 'recipe not found', 'detail': 'Not found'})
        serializer = RecipeCreateSerializer(data=recipe_data, instance=recipe, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        deleted_recipe_count, data = Recipe.objects.filter(slug=slug, is_published=True).delete()
        print(deleted_recipe_count)
        if deleted_recipe_count == 0:
            raise NotFound({'message': 'recipe not found', 'detail': 'Not found'})
        return Response({}, status=HTTP_204_NO_CONTENT)
