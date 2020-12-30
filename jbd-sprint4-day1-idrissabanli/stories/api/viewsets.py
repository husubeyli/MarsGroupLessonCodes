from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from stories.api.serializers import RecipeSerializer, RecipeCreateSerializer, TagSerializer, CategorySerializer
from stories.models import Recipe, Tag, Category


class TagViewSet(ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(is_published=True)


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_published=True)


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeCreateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Recipe.objects.filter(is_published=True)
    serializers = {
        'list': RecipeSerializer,
        'retrieve': RecipeSerializer,
        'update': RecipeCreateSerializer,
        'partial_update': RecipeCreateSerializer,
        'delete': RecipeCreateSerializer,
        'create': RecipeCreateSerializer,
        'default': RecipeCreateSerializer,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        category_ids = self.request.GET.get('category_ids')
        sort_by = self.request.GET.get('sort_by')
        if category_ids:
            category_ids = category_ids.split(',')
            queryset = queryset.filter(category__id__in=category_ids)
        if sort_by and getattr(Recipe, sort_by, False):
            queryset = queryset.order_by(sort_by)
        return queryset

    def get_serializer_class(self):
        # print(self.action)
        return self.serializers.get(self.action, self.serializers.get('default'))
