from django.urls import path

from accounts.api.views import CustomAuthToken, UserRegisterAPIView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='auth_login'),
    path('register/', UserRegisterAPIView.as_view(), name='auth_register'),
]