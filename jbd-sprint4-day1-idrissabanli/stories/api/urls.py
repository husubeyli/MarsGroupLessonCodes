from django.urls import path
from stories.api.routers import router

from stories.api.views import (
    RecipeAPIView,
    RecipeRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    # path('recipes/', RecipeAPIView.as_view(), name='recipes'),
    # path('recipes/<slug:slug>/', RecipeRetrieveUpdateDeleteAPIView.as_view(), name='recipe'),
] + router.urls
