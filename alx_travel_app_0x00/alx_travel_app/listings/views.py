"""
listings/views.py
-----------------
Request handlers for the /api/listings/ endpoint.

We start with DRF’s generic class‑based views so we get CRUD quickly.
"""

from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/listings/   -> list all listings
    POST /api/listings/   -> create a new listing
    """
    queryset = Listing.objects.all().order_by("-created_at")  # newest first
    serializer_class = ListingSerializer