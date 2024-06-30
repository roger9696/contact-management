from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

# Create your views here.
class ContactListCreate(generics.ListCreateAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer


class ContactRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  lookup_field = 'pk'
