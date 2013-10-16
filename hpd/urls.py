from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hpd.views.home', name='home'),
    # url(r'^hpd/', include('hpd.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
