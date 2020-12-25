from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from stories.api.serializers import (
    RecipeSerializer,
    RecipeCreateSerializer
)
from stories.models import (
    Recipe,
)


class RecipeAPIView(APIView):

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
