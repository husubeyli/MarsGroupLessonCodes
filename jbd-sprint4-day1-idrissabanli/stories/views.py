from django.shortcuts import render
from django.http import Http404
from datetime import datetime

users = [
    {
        'id': 1,
        'name': 'Kenan salam',
        'desc': '''<h1>Lorem ipsum, dolor sit amet 
        consectetur adipisicing elit. Numquam error 
        aperiam sint laboriosam deserunt impedit quibusdam aut 
        consequatur pariatur autem exercitationem, 
        fuga iure, omnis quo in 
        ipsam nihil perferendis ipsum.</h1>''',
        'birth_day': datetime.now()
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
