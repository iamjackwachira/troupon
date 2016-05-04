"""Base url configuration for DRF.

The `urlpatterns` list routes URLs to the API views.
Example:
Using Class-based views
    1. Add an import:  from some_app.api import HomeAPIView
    2. Add a URL to urlpatterns:
        url(r'^api/home/$', HomeApiView.as_view(), name='home_api')
"""
from django.conf.urls import include, url
from merchant.api import DealListAPIView, DealActionsAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # URL definition for API goes here.
    url(r'^deals/$', DealListAPIView.as_view()),
    url(r'^deals/(?P<pk>[0-9]+)$', DealActionsAPIView.as_view()),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)