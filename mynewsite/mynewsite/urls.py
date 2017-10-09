from django.conf.urls import include, url
from django.contrib import admin
from mvctest.views import about,index
from phone.views import listting,disp_detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', about),
    url(r'^list/$', listting),
    url(r'^list/([0-9a-zA-z]+)/$', disp_detail),
    url(r'^$', index),
]
