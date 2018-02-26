from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login

urlpatterns = [
    # Example:
    # url(r'^idptest/', include('idptest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Required for login:
    url(r'^accounts/login/$', login),

    # URLs for the IDP:
    url(r'^idp/', include('saml2idp.urls')),
]
