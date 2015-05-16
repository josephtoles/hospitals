from django.shortcuts import render
from data.models import Hospital


def home(request):
    #TODO pick the best page to show here instead
    return render(request, 'base.html')


def search(request):
    return render(request, 'base.html')


def map(request):
    return render(request, 'map.html')


def top(request):
    context = {'hospitals': Hospital.objects.order_by('quality', 'atmosphere', 'price').all()}
    return render(request, 'top.html', context)


def nerd_stuff(request):
    return render(request, 'base.html')


def news(request):
    return render(request, 'news.html')


def about(request):
    return render(request, 'base.html')
