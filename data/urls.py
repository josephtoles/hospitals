from django.conf.urls import patterns, url


urlpatterns = patterns(
    'data.views',
    url(r'^upload_csv_with_coordinates', 'upload_csv_with_coordinates', name='upload_csv_with_coordinates'),  # TODO fix naming convention
    url(r'^upload_csv', 'upload_csv_without_coordinates', name='upload_csv'),  # TODO fix naming convention
    url(r'^get_json', 'get_json', name='get_json'),
    url(r'^download_csv', 'download_csv', name='download_csv'),
)