from django.urls import path

from stories.api.views import (
    RecipeAPIView,
)

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(), name='recipes'),
]
