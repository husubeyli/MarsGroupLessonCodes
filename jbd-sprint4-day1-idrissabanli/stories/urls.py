from math import nan
from django.urls import path
from stories.views import (
    test,
    home,
    user_detail,
    # contact,
    # recipe_list,
    RecipeListView,
    RecipeDetailView,
    ContactCreateView,
    CreateRecipeView,
    UpdateRecipeView, 
    RecipeDeleteView,
    AboutView
) 

app_name = 'stories'


urlpatterns = [
    path('test/', test, name='test_page'),
    path('', home, name='home_page'),
    path('about/', AboutView.as_view(), name='about'),
    path('user-detail/<int:user_id>/', user_detail, name='user_detail'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe-detail/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('update-recipe/<int:pk>/', UpdateRecipeView.as_view(), name='recipe_update'),
    path('create-recipe/', CreateRecipeView.as_view(), name='create_recipe'),
    path('delete-recipe/<int:pk>/', RecipeDeleteView.as_view(), name='delete_recipe')
]