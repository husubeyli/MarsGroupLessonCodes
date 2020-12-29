from django.urls import path, re_path, include
from django.contrib.auth.views import LogoutView
from accounts.views import (
    RegisterView,
    UserActivate,
    UserProfileView,
    CustomLoginView,
    CustomPasswordChangeView,
    PasswordChangeDone,
    CustomPasswordResetView,
    PasswordResetDone,
    PasswordResetCompletedView,
    CustomPasswordResetConfirmView
)

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('forget-password/', CustomPasswordResetView.as_view(), name='forget_password'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            UserActivate.as_view(), name='activate'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<slug:username>/', UserProfileView.as_view(), name='profile'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDone.as_view(), name='password_change_done'),
    path('password-reset-done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset-completed/', PasswordResetCompletedView.as_view(), name='password_reset_completed'),
    re_path(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/v1.0/', include('accounts.api.urls'))
]
