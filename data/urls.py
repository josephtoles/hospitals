from django.conf.urls import patterns, url


urlpatterns = patterns(
    'data.views',
    url(r'^upload_csv', 'upload_csv', name='upload_csv'),
    url(r'^get_json', 'get_json', name='get_json')
)