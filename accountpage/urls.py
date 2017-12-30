"""accountpage URL Configuration
"""
from django.conf.urls import url
from accountpage.views import test_view

urlpatterns = [
    url('profile/', test_view),
]
