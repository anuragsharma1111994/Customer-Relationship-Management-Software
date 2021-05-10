from django.test import TestCase
from django.shortcuts import resolve_url

class LandingPageTest(TestCase):
    def test_get(self):
        response = self.client.get(resolve_url("landing-page"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"landing.html")
