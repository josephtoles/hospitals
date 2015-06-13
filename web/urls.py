from django.conf.urls import patterns, url


urlpatterns = patterns(
    'web.views',
    url(r'^contact', 'contact', name='contact'),
    url(r'^disclaimer', 'disclaimer', name='disclaimer'),
    url(r'^hospital/(?P<id>[0-9]+)', 'hospital', name='hospital'),
    url(r'^about', 'about', name='about'),
    url(r'^test', 'test', name='test'),
)