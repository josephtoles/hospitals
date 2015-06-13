from django.shortcuts import render
from data.models import Hospital
from models import ContactMessage
from django.shortcuts import get_object_or_404


#TODO make this more efficient
def get_default_context():
    cities = sorted(set([d['city'] for d in Hospital.objects.values('city')]))
    return {
        'cities': cities,
    }


def hospital(request, id):
    context = get_default_context()
    context['hospital'] = get_object_or_404(Hospital, id=id)
    return render(request, 'hospital.html', context)


def contact(request):
    context = get_default_context()
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']
        ContactMessage.objects.create(email=email, message=message)
    context['message_sent'] = request.method == 'POST'
    return render(request, 'contact.html', context)


def disclaimer(request):
    return render(request, 'disclaimer.html', get_default_context())


def home(request):
    context = get_default_context()
    selected_city = None
    if request.method == 'POST':
        city = request.POST['city']
        results_queryset = Hospital.objects.order_by('-quality')
        results_queryset = results_queryset.filter(quality__gt=0)     # removes hospitals without data
        results_queryset = results_queryset.filter(atmosphere__gt=0)  # removes hospitals without data
        results_queryset = results_queryset.filter(price__gt=0)       # removes hospitals without data
        if city:
            results_queryset = results_queryset.filter(city=city)
            selected_city = city
        results = results_queryset.all()
        cities = sorted(set([d['city'] for d in Hospital.objects.values('city')]))
        context.update({
            'cities': cities,
            'results': results,
            'selected_city': selected_city,
        })
        return render(request, 'search.html', context)
    else:
        return render(request, 'home.html', get_default_context())


def about(request):
    return render(request, 'about.html', get_default_context())


# Just to make testing easier
def test(request):
    return render(request, 'test_template.html', get_default_context())