from django.shortcuts import render
from django.http import HttpResponseBadRequest
from models import Hospital
import csv


def upload_csv(request):
    if request.method == 'POST':
        csvfile = request.FILES['datafile']
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        listified = [row for row in spamreader]
        if listified[0] != [
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
            'Price']:
            return HttpResponseBadRequest()
        Hospital.objects.all().delete()
        for i in range(1, len(listified)):
            datum =  listified[i]
            # import pdb; pdb.set_trace()
            Hospital.objects.create(
                provider_id=int(datum[0]),
                name=datum[1],
                address=datum[2],
                city=datum[3],
                state=datum[4],
                zip_code=int(datum[5]),
                county_name=datum[6],
                phone_number=int(datum[7]),
                quality=float(datum[8]),
                atmosphere=float(datum[9]),
                price=float(datum[10]),
            )
        return render(request, 'upload_csv.html', {'done': True})
    return render(request, 'upload_csv.html', {'done': False})
