from django.shortcuts import render
from django.http import Http404

users = [
    {
        'id': 1,
        'name': 'Kenan'
    },
    {
        'id': 2,
        'name': 'Turqut'
    },
    {
        'id': 3,
        'name': 'Murad'
    }
]

def test(request):
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
