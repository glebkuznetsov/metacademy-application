from django.conf.urls import patterns, include, url
# handle static files locally
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.cache import cache_page
from backend.views import get_kmap_browser_view, get_search_view, get_landing_page

"""
Django urls handler. Valid URLS/Requests:
  kmap(s)                           display knowledge-map browser

see backend/simple_server for valid content requests
"""

urlpatterns = patterns('',
                       (r'^$', get_landing_page),
                       (r'^(?i)kmaps?/', get_kmap_browser_view),
                       (r'^(?i)search', get_search_view)
)

urlpatterns += staticfiles_urlpatterns()
