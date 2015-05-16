from django.shortcuts import render


def home(request):
    #TODO pick the best page to show here instead
    return render(request, 'base.html')


def search(request):
    return render(request, 'base.html')


def map(request):
    return render(request, 'base.html')


def top_100(request):
    return render(request, 'base.html')


def nerd_stuff(request):
    return render(request, 'base.html')


def news(request):
    return render(request, 'news.html')


def about(request):
    return render(request, 'base.html')
