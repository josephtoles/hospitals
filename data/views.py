from django.shortcuts import render
from django.http import HttpResponseBadRequest
from models import Hospital
import csv


def upload_csv(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
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
            import pdb; pdb.set_trace()
            return HttpResponseBadRequest()
        # import pdb; pdb.set_trace()
        Hospital.objects.all().delete()

        def string_to_float(s):
            try:
                return float(s)
            except ValueError:
                return None

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
                quality=string_to_float(datum[8]),
                atmosphere=string_to_float(datum[9]),
                price=string_to_float(datum[10]),
            )
        return render(request, 'upload_csv.html', {'done': True})
    return render(request, 'upload_csv.html', {'done': False})
