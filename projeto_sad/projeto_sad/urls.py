from django.conf.urls import patterns, include, url
from django.contrib import admin
from vigilante.views import home, get_eventos_json

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projeto_sad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^json/pontos/(?P<tipo>)$', get_eventos_json)
)
