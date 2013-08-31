from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.list_detail import object_list
from django.conf import settings
admin.autodiscover() 
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^news/', include('news.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'views.index'),
    (r'^index/$', 'views.index'),
    (r'^index/main.html$', 'views.main'),
    (r'^index/top.html$', 'views.top'),
    (r'^index/foot.html$', 'views.foot'),
    (r'^admin/(.*)', admin.site.root),
    (r'^mydomain/$', 'common_user.views.logindex'),
    (r'^reg/$', 'common_user.views.reg'),
    (r'^login/$', 'common_user.views.login'),
    (r'^logout/$', 'common_user.views.logout'),
    (r'^register/$', 'common_user.views.register'),
    (r'^password/$', 'common_user.views.password'),
    (r'^setpassword/$', 'common_user.views.set_password'),
    (r'^train/$', 'train.views.index'),
    (r'^news/', include('bttis.news.urls')),
    (r'^ticketQuery/$', 'ticket.views.index'),
    (r'^ticket/', include('bttis.ticket.urls')),
    (r'^ticket/(\d+)/$', 'ticket.views.post_info'),
    (r'^news/(\d+)/$', 'news.views.display'),
    (r'^trainQuery/stationToStation$', 'train.views.query_station_station'),
    (r'^trainQuery/trainNum$', 'train.views.query_trainNum'),
    (r'^trainQuery/station$', 'train.views.query_station'),
    (r'^ticketQuery/stationToStation$', 'ticket.views.query_station_station'),
    (r'^ticketQuery/trainNum$', 'ticket.views.query_trainNum'),
    (r'^(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_PATH}),
)