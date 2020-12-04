from django.shortcuts import render
from django.http import Http404
from datetime import datetime

from stories.models import Author


def test(request):
    users = Author.objects.all()
    context = {
        'user_list': users
    }
    return render(request, 'users.html', context)


def user_detail(request, user_id):
    # if user_id > len(users):
    #     raise Http404
    user = users[user_id-1]
    # print(request.GET)
    # user = request.GET.get('selected_user', 'Secilmis User yoxdur')
    context = {
        'selected_user': user
    }
    return render(request, 'user_detail.html', context)


def home(request):
    return render(request, 'index.html')
