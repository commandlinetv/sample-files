from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url('^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'etutor.views.home', name='home'),
    # url(r'^etutor/', include('etutor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
