from django.conf.urls.defaults import *
from django.contrib import admin
from bttis.news.models import List
from bttis.news.models import Item
admin.autodiscover() 
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

info_dict = {
    'queryset':Item.objects.all(),
    'template_name':'news/news_list.html'
    }
urlpatterns = patterns('',
    # Example:
    # (r'^news/', include('news.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^/?$', 'django.views.generic.list_detail.object_list', info_dict)
    
)