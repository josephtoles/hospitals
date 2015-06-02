from django.conf.urls import patterns, url


urlpatterns = patterns(
    'web.views',
    # url(r'^/$', 'home', name='home'),
    url(r'^map', 'map', name='map'),
    # url(r'^top', 'top', name='top'),
    url(r'^contact', 'contact', name='contact'),
    url(r'^disclaimer', 'disclaimer', name='disclaimer'),
    url(r'^hospital/(?P<id>[0-9]+)', 'hospital', name='hospital'),
    url(r'^nerd_stuff', 'nerd_stuff', name='nerd_stuff'),
    url(r'^news', 'news', name='news'),
    url(r'^about', 'about', name='about'),
)