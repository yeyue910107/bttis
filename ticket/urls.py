from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover() 
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Example:
    # (r'^news/', include('news.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^/?$', 'django.views.generic.list_detail.object_list', info_dict)
    (r'^post_step1/$', 'ticket.views.post_step1'),
    (r'^post_step2/$', 'ticket.views.post_step2'),
    (r'^post/$', 'ticket.views.post'),
    (r'^mypost/$', 'ticket.views.mypost'),
    (r'^mypost_info/(\d+)/$', 'ticket.views.mypost_info')
)