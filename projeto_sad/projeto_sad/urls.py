from django.conf.urls import patterns, include, url
from django.contrib import admin
import vigilante
from vigilante.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projeto_sad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', home,),
    url(r'^/', home,),
    url(r'^/?P<endereco>', home,), #escrever regex
)
