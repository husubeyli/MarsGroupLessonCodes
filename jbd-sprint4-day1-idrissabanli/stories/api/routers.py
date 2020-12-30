from rest_framework.routers import DefaultRouter

from stories.api.viewsets import RecipeViewSet, TagViewSet, CategoryViewSet

router = DefaultRouter()

router.register('recipes', RecipeViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
