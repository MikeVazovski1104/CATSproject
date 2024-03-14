from django.http import HttpResponse
from rest_framework import generics

from .models import Guest, Pets
from .serializer import GuestSerializer


class GuestAPIView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

def hello_cats(request):
    return HttpResponse("Hello from cats")