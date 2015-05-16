from django.conf.urls import patterns, url


urlpatterns = patterns(
    'web.views',
    url(r'^search', 'search', name='search'),
    url(r'^map', 'map', name='map'),
    url(r'^top_100', 'top_100', name='top_100'),
    url(r'^nerd_stuff', 'nerd_stuff', name='nerd_stuff'),
    url(r'^news', 'news', name='news'),
    url(r'^about', 'about', name='about'),
)