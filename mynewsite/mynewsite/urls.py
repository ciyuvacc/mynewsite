from django.conf.urls import include, url
from django.contrib import admin
from mvctest.views import about
from phone.views import listting

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', about),
    url(r'^list/', listting),
]
