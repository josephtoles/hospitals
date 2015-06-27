from django.conf.urls import patterns, url


urlpatterns = patterns(
    'data.views',
    url(r'^upload_csv', 'upload_csv', name='upload_csv'),  # TODO fix naming convention
    url(r'^get_json', 'get_json', name='get_json'),
    url(r'^download_csv', 'download_csv', name='download_csv'),
)