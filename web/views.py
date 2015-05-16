from django.shortcuts import render
from data.models import Hospital


def home(request):
    #TODO pick the best page to show here instead
    return render(request, 'base.html')


def search(request):
    states = sorted(set([d['state'] for d in Hospital.objects.values('state')]))
    cities = sorted(set([d['city'] for d in Hospital.objects.values('city')]))
    context = {'states': states, 'cities': cities}
    return render(request, 'search.html', context)


def map(request):
    return render(request, 'map.html')


def top(request):
    context = {'hospitals': Hospital.objects.order_by('quality', 'atmosphere', 'price').all()}
    return render(request, 'top.html', context)


def nerd_stuff(request):
    return render(request, 'nerd_stuff.html')


def news(request):
    return render(request, 'news.html')


def about(request):
    return render(request, 'base.html')
