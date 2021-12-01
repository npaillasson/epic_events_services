from django.test import TestCase, Client
from accounts.models import User
from django.urls import reverse, resolve
from django.contrib.auth.models import Group

class LoginPageTests(TestCase):

    def setUp(self):
        print(Group.objects.all())
        User.objects.create_user(email='test@gestion.com', password="HDIB9DPZBDNS5",
                                 first_name="John", last_name="Doe", team="1")
        User.objects.create_user(email='test@client.com', password="HDIB9DPZBDNS5",
                                 first_name="John", last_name="Doe", team="2")
        User.objects.create_user(email='test@support.com', password="HDIB9DPZBDNS5",
                                 first_name="John", last_name="Doe", team="3")

    def test_csrf(self):
        url = resolve("/EpicEvents/CRM_acces/")
        response = self.client.get(url)
        self.assertContains(response.content, "csrfmiddlewaretoken")

# Create your tests here.
