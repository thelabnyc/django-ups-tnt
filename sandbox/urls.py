from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('ups_tnt.urls')),
    url(r'^admin/', admin.site.urls),
]
