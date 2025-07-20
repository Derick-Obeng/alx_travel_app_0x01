"""
listings/urls.py
----------------
Routes for the listings app – included from project‑level urls.py.
"""

from django.urls import path
from .views import ListingListCreateView

urlpatterns = [
    # /api/listings/
    path("listings/", ListingListCreateView.as_view(), name="listing-list-create")
]