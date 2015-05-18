from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from data.models import Hospital, RequestsRecord
from urllib2 import urlopen, HTTPError
import time
import json


API_KEY = 'AIzaSyBBSCmmD23WqE0414ruTyXWQwHGKO4e2_8'
MAX_DAILY_REQUESTS = 2500


class Command(BaseCommand):

    def handle(self, *args, **options):
        while(True):
            # Google does this check for you
            '''
            # TODO re-write this with get_object_or_create
            # Check daily throttling
            try:
                record = RequestsRecord.objects.get(date=now().date())
                record.requests = record.requests + 1
                record.save()
                if record.requests >= MAX_DAILY_REQUESTS:
                    print 'You have reached your maximum requests for the day'
                    return
            except RequestsRecord.DoesNotExist:
                RequestsRecord.objects.create(date=now().date(), requests=1)
            '''

            # Get data for a hospital
            hospital = Hospital.objects.filter(lat=None, lng=None, coordinates_unknown=False).first()  # hospital to update
            if hospital is None:
                print 'All Hospitals have coordinates'
                return True
            address = hospital.address.replace(' ', '+')
            city = hospital.city.replace(' ', '+')
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address={address},+{city},+{state}&key={key}'.format(
                address=address, city=city, state=hospital.state, key=API_KEY)
            response = urlopen(url)
            text = response.read()
            parsed = json.loads(text)
            if parsed['status'] == 'ZERO_RESULTS':
                print 'coordinates unknown for {}'.format(hospital.name)
                hospital.coordinates_unknown = True
                hospital.save()
            elif parsed['status'] == "OVER_QUERY_LIMIT":
                print 'You have exceeded your daily request quota for this API.'
                # record = RequestsRecord.objects.get(date=now().date())
                # record.requests = MAX_DAILY_REQUESTS
                # record.save()
                return
            elif parsed['status'] != 'OK':
                print 'return status is not "OK"'
                print 'output is %s' % text
                import pdb
                pdb.set_trace()
                return
            else:
                lat = parsed['results'][0]['geometry']['location']['lat']
                lng = parsed['results'][0]['geometry']['location']['lng']
                print ('got coordinates ({}, {}) for hospital {}. '.format(lat, lng, hospital.name))
                hospital.lat = lat
                hospital.lng = lng
                hospital.save()
            time.sleep(0.25)
