from django.test import TestCase, Client
from accounts.models import User
from django.urls import reverse, resolve
from django.contrib.auth.models import Group
from epic_events_services import urls

PASSWORD_TEST = "HDIB9DPZBDNS5"
GESTION_USER_EMAIL = "test@gestion.com"
BUSINESS_USER_EMAIL = "test@client.com"
SUPPORT_USER_EMAIL = "test@support.com"


class LoginPageTests(TestCase):

    fixtures = ["data_for_test.json"]

    def setUp(self):
        User.objects.create_user(
            email=GESTION_USER_EMAIL,
            password=PASSWORD_TEST,
            first_name="John",
            last_name="Doe",
            team="1",
        )
        User.objects.create_user(
            email=BUSINESS_USER_EMAIL,
            password=PASSWORD_TEST,
            first_name="John",
            last_name="Doe",
            team="2",
        )
        User.objects.create_user(
            email=SUPPORT_USER_EMAIL,
            password=PASSWORD_TEST,
            first_name="John",
            last_name="Doe",
            team="3",
        )

    def test_csrf(self):
        response = self.client.get(f"/{urls.BASE_URL}", follow=True)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_gestion_teamate_can_connect(self):
        user = User.objects.get(email=GESTION_USER_EMAIL)
        connect = self.client.login(username=user.username, password=PASSWORD_TEST)
        self.assertEqual(connect, True)

    def test_business_teamate_can_connect(self):
        user = User.objects.get(email=BUSINESS_USER_EMAIL)
        connect = self.client.login(username=user.username, password=PASSWORD_TEST)
        self.assertEqual(connect, True)

    def test_support_teamate_can_connect(self):
        user = User.objects.get(email=SUPPORT_USER_EMAIL)
        connect = self.client.login(username=user.username, password=PASSWORD_TEST)
        self.assertEqual(connect, True)

    def test_login_fail_with_bad_identifiers(self):
        connect = self.client.login(username="fake_username", password="Bad_password")
        self.assertEqual(connect, False)
