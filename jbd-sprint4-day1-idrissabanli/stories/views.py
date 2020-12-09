import math
from django.shortcuts import render, redirect
from django.http import Http404, request
from datetime import datetime
from django.db.models import Q

from stories.models import Author, Contact
from stories.forms import (
    ContactForm
)


def test(request):
    users = Author.objects.all()
    searched_name = request.GET.get('search')
    order_by = request.GET.get('order')
    per_count = 3
    print(searched_name)
    page = int(request.GET.get('page', 1))
    if searched_name:
        users = users.filter(Q(first_name__icontains=searched_name) 
        | Q(last_name__icontains=searched_name))
    if order_by:
        users = users.order_by(order_by)

    page_count = math.ceil(users.count()/per_count)
    users = users[(page-1)*per_count:page*per_count]
    page_range = range(1, page_count+1)
    context = {
        'user_list': users,
        'current_page': page,
        'searched_name': searched_name if searched_name else '',
        'page_range': page_range
    }
    return render(request, 'users.html', context)


def user_detail(request, user_id):
    # if user_id > len(users):
    #     raise Http404
    user = []
    # print(request.GET)
    # user = request.GET.get('selected_user', 'Secilmis User yoxdur')
    context = {
        'selected_user': user
    }
    return render(request, 'user_detail.html', context)


def home(request):
    return render(request, 'index.html')


def contact(request):
    form  = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            #name = form.cleaned_data['name']
            #email = form.cleaned_data['email']
            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            #contact = Contact(name=name, email=email, subject=subject, message=message)
            #contact.save()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
