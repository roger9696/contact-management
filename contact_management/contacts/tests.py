
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Contact

class ContactTests(APITestCase):
    def test_create_contact(self):
        url = reverse('contact-list-create')
        data = {'name': 'John Doe', 'phone_number': '1234567890'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_contacts(self):
        url = reverse('contact-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_contact(self):
        contact = Contact.objects.create(name='John Doe', phone_number='1234567890')
        url = reverse('contact-detail', args=[contact.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_contact(self):
        contact = Contact.objects.create(name='John Doe', phone_number='1234567890')
        url = reverse('contact-detail', args=[contact.id])
        data = {'name': 'Jane Doe', 'phone_number': '0987654321'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_contact(self):
        contact = Contact.objects.create(name='John Doe', phone_number='1234567890')
        url = reverse('contact-detail', args=[contact.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
