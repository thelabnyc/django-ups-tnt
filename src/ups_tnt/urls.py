from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TimeInTransitView


urlpatterns = [
    re_path(r"^tnt/$", TimeInTransitView.as_view(), name="time-in-transit"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
