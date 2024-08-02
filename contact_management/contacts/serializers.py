from rest_framework import serializers
from .models import Contact
import re

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = '__all__'



    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError('Invalid email format')
        return value

    def validate_phone(self, value):
        if not value.strip():
            raise serializers.ValidationError("Phone number cannot be empty")
        return value


