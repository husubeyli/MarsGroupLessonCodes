from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import CustomUserCreationForm, LoginForm, CustomPasswordChangeForm, CustomPasswordResetForm, \
    CustomSetPasswordForm
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from accounts.tasks import send_confirmation_email
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import success, error
from django.views.generic import (
    CreateView,
    View,
    TemplateView,
    DetailView
)

from accounts.tools.tokens import account_activation_token
from stories.models import Recipe

User = get_user_model()


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        site_address = self.request.is_secure() and "https://" or "http://" + self.request.META['HTTP_HOST']  # https
        # ://stackoverflow.com/
        send_confirmation_email(user, site_address)
        return super().form_valid(form)


# def register(request):
#     form = CustomUserCreationForm()
#     if request.method == 'POST':
#         form = CustomUserCreationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https://stackoverflow.com/
#             send_confirmation_email(user, site_address)
#             return redirect(reverse_lazy('accounts:login'))
#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)

class UserActivate(View):

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            success(request, 'Email is activated')
            return redirect(reverse_lazy('accounts:login'))
        else:
            error(request, 'Email is not activated')
            return redirect(reverse_lazy('accounts:register'))


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('accounts:password_change_done')


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'password_change_done.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'forget_password.html'
    email_template_name = 'email/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:password_reset_completed')


class PasswordResetCompletedView(PasswordResetCompleteView):
    template_name = 'password_reset_completed.html'


class UserProfileView(DetailView):
    template_name = 'user-profile.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'
    model = User

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super(UserProfileView, self).get_context_data(**kwargs)
        recipes = Recipe.objects.filter(owner=user)
        context['recipes'] = recipes
        return context


# class UserProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'user-profile.html'
#     # model = User
#
#     def get_context_data(self, **kwargs):
#         user = self.request.user
#         context = super(UserProfileView, self).get_context_data(**kwargs)
#         recipes = Recipe.objects.filter(owner=user)
#         context['recipes'] = recipes
#         return context
#         # stories = Story.objects.filter()
        



# def login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
#             if user:
#                 django_login(request, user)
#                 success(request, f'Xos geldin {user.get_full_name()}')
#                 return redirect(reverse_lazy('stories:home_page'))
#             else:
#                 error(request, 'Istifadeci adi ve ya sifre yalnisdir')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)
