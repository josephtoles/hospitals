from django.shortcuts import render
from data.models import Hospital
from models import ContactMessage
from django.shortcuts import get_object_or_404


def hospital(request, id):
    hospital = get_object_or_404(Hospital, id=id)
    return render(request, 'hospital.html', {'hospital': hospital})


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        ContactMessage.objects.create(email=email, message=message)
        return render(request, 'contact.html', {'message_sent': True})
    else:
        return render(request, 'contact.html', {'message_sent': False})


def disclaimer(request):
    return render(request, 'disclaimer.html')


def home(request):
    selected_state = None
    selected_city = None
    if request.method == 'POST':
        city = request.POST['city']
        state = request.POST['state']
        results_queryset = Hospital.objects.order_by('-quality')
        results_queryset = results_queryset.filter(quality__gt=0)  # removes hospitals without data
        results_queryset = results_queryset.filter(atmosphere__gt=0)  # removes hospitals without data
        results_queryset = results_queryset.filter(price__gt=0)  # removes hospitals without data
        if city:
            results_queryset = results_queryset.filter(city=city)
            selected_city = city
        if state:
            results_queryset = results_queryset.filter(state=state)
            selected_state = state
        results = results_queryset.all()
    else:
        results = None

    states = sorted(set([d['state'] for d in Hospital.objects.values('state')]))
    cities = sorted(set([d['city'] for d in Hospital.objects.values('city')]))
    context = {
        'states': states,
        'cities': cities,
        'results': results,
        'selected_state': selected_state,
        'selected_city': selected_city,
    }
    return render(request, 'search.html', context)


def map(request):
    context = {'hospitals': Hospital.objects.filter(lat__gt=0, lng__lt=0).all()}
    return render(request, 'location.html', context)
    # return render(request, 'map.html')


def top(request):
    context = {'hospitals': Hospital.objects.order_by('quality', 'atmosphere', 'price').all()}
    return render(request, 'top.html', context)


def nerd_stuff(request):
    return render(request, 'nerd_stuff.html')


def news(request):
    return render(request, 'news.html')


def about(request):
    return render(request, 'about.html')
