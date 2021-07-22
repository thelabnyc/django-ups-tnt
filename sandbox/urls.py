from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

urlpatterns = [
    re_path(r"^api/", include("ups_tnt.urls")),
    re_path(r"^admin/", admin.site.urls),
]
