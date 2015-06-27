from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.utils import DataError
from django.forms.models import model_to_dict
from django.utils.timezone import now
from models import Hospital
import csv
import json
import pytz


# Gets data for AJAX JavaScript
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


# Generates a CSV of the data in the server
def download_csv(request):
    if request.user.is_authenticated():
        if not request.user.is_staff:
            return HttpResponseForbidden()
    else:
        return HttpResponseRedirect('/admin/login/?next=%s' % reverse('upload_csv'))  # TODO clean this up
    response = HttpResponse(content_type='text/csv')
    timestamp = now().astimezone(pytz.timezone('America/Los_Angeles')).strftime('%Y-%m-%d_T%H-%M-%S')
    filename = 'Hospital_data_{timestamp}.csv'.format(timestamp=timestamp)
    response['Content-Disposition'] = 'attachment; filename="{filename}"'.format(filename=filename)
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
        'Price',
        'lat',
        'lng',]

    writer = csv.writer(response)
    writer.writerow([value for value in CORRECT_VALUES])
    for hospital in Hospital.objects.all():
        writer.writerow([
            hospital.provider_id,
            hospital.name,
            hospital.address,
            hospital.city,
            hospital.state,
            hospital.zip_code,
            hospital.county_name,
            hospital.phone_number,
            hospital.quality,
            hospital.atmosphere,
            hospital.price,
            hospital.lat,
            hospital.lng,
        ])

    return response


def upload_csv_with_coordinates(request):
    return upload_csv(request, True)


def upload_csv_without_coordinates(request):
    return upload_csv(request, False)


def upload_csv(request, include_coordinates):
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
        if include_coordinates:
            CORRECT_VALUES.append('lat')
            CORRECT_VALUES.append('lng')
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
                if include_coordinates:
                    hospital.lat=string_to_float(datum[11])
                    hospital.lng=string_to_float(datum[12])
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
                        lat=string_to_float(datum[11]),
                        lng=string_to_float(datum[12]),
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
                        lat=string_to_float(datum[11]),
                        lng=string_to_float(datum[12]),
                    )
        return render(request, 'upload_csv.html', {'done': True})
    return render(request, 'upload_csv.html', {'done': False})
