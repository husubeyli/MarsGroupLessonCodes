from rest_framework.routers import DefaultRouter

from stories.api.viewsets import RecipeViewSet

router = DefaultRouter()

router.register('recipes', RecipeViewSet)
