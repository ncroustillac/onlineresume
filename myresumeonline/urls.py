from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myresumeonline/', include('myresumeonline.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^index/$','onlineresume.views.index'),
    (r'^index/(?P<content>\w+)$', 'onlineresume.views.index'),
    (r'^education/$', 'onlineresume.views.education'),
    (r'^experience/$', 'onlineresume.views.experience'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        # personale computer path
        # {'document_root': '/home/ncroustillac/Dropbox/Public/mysite/myresumeonline/media'}),
        # laptop path
        { 'document_root': '/home/nil/partage/dev/onlineresume/myresumeonline/media'}),
)

