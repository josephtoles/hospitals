from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.utils import DataError
from django.forms.models import model_to_dict
from models import Hospital
import csv
import json


def get_json(request):
    #TODO remove code duplication
    city = request.GET.get('city', None)
    state = request.GET.get('state', None)
    results_queryset = Hospital.objects.order_by('-quality')
    results_queryset = results_queryset.filter(quality__gt=0)  # removes hospitals without data
    results_queryset = results_queryset.filter(atmosphere__gt=0)  # removes hospitals without data
    results_queryset = results_queryset.filter(price__gt=0)  # removes hospitals without data
    if city:
        results_queryset = results_queryset.filter(city=city)
    if state:
        results_queryset = results_queryset.filter(state=state)
    results = results_queryset.all()
    dict_results = [model_to_dict(result) for result in results]
    string = json.dumps(dict_results)
    return HttpResponse(string, content_type='application/json')


def upload_csv(request):
    if request.user.is_authenticated():
        if not request.user.is_staff:
            return HttpResponseForbidden()
    else:
        return HttpResponseRedirect('/admin/login/?next=%s' % reverse('upload_csv'))  # TODO clean this up
    if request.method == 'POST':
        csvfile = request.FILES['datafile']
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        listified = [row for row in spamreader]
        CORRECT_VALUES = [
            'Provider ID',
            'Hospital Name',
            'Address',
            'City',
            'State',
            'ZIP Code',
            'County Name',
            'Phone Number',
            'Quality',
            'Atmosphere',
            'Price']
        if listified[0] != CORRECT_VALUES:
            return HttpResponseBadRequest()

        def string_to_float(s):
            try:
                return float(s)
            except ValueError:
                return None

        for i in range(1, len(listified)):
            datum =  listified[i]
            try:
                hospital = Hospital.objects.get(provider_id=int(datum[0]))
                hospital.provider_id=int(datum[0])
                hospital.name=datum[1]
                hospital.address=datum[2]
                hospital.city=datum[3]
                hospital.state=datum[4]
                hospital.zip_code=int(datum[5])
                hospital.county_name=datum[6]
                hospital.phone_number=int(datum[7])
                hospital.quality=string_to_float(datum[8])
                hospital.atmosphere=string_to_float(datum[9])
                hospital.price=string_to_float(datum[10])
                hospital.save()
            except Hospital.DoesNotExist:
                try:
                    Hospital.objects.create(
                        provider_id=int(datum[0]),
                        name=datum[1],
                        address=datum[2],
                        city=datum[3],
                        state=datum[4],
                        zip_code=int(datum[5]),
                        county_name=datum[6],
                        phone_number=int(datum[7]),
                        quality=string_to_float(datum[8]),
                        atmosphere=string_to_float(datum[9]),
                        price=string_to_float(datum[10]),
                    )
                except DataError:  # integer out of range
                    Hospital.objects.create(
                        provider_id=int(datum[0]),
                        name=datum[1],
                        address=datum[2],
                        city=datum[3],
                        state=datum[4],
                        zip_code=int(datum[5]),
                        county_name=datum[6],
                        phone_number=0,
                        quality=string_to_float(datum[8]),
                        atmosphere=string_to_float(datum[9]),
                        price=string_to_float(datum[10]),
                    )
        return render(request, 'upload_csv.html', {'done': True})
    return render(request, 'upload_csv.html', {'done': False})
