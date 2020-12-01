from django.shortcuts import render


def test(request):
    print('salam')
    return render(request, 'test.html')

def home(request):
    print('salam')
    return render(request, 'index.html')