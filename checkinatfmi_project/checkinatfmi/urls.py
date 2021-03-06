from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.sites.models import Site


admin.autodiscover()
admin.site.unregister(Site)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^checkin/', include('clients.urls')),
    url(r'^activities/', include('activities.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'website.views.logout_page'),

    url(r'', include('website.urls')),
)
