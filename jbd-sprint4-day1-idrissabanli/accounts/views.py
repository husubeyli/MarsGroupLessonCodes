from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.tasks import send_confirmation_email
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.messages import success, error

from accounts.tools.tokens import account_activation_token

User = get_user_model()


def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https://stackoverflow.com/
            send_confirmation_email(user, site_address)
            return redirect(reverse_lazy('accounts:login'))
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        success(request, 'Email is activeted')
        return redirect(reverse_lazy('accounts:login'))
    else:
        error(request, 'Email is not activeted')
        return redirect(reverse_lazy('accounts:register'))


def login(request):
    return render(request, 'login.html')

