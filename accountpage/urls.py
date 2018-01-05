"""accountpage URL Configuration
"""
from django.conf.urls import url
from accountpage.views import *

urlpatterns = [
    url(r'profile/', profile_view),
    url(r'add_card/', add_card_view),
    url(r'remove_card/([^/]+)/', remove_card_view),
    url(r'make_default_card/([^/]+)/', make_default_card_view),
    url(r'subscribe/', subscribe),
]
