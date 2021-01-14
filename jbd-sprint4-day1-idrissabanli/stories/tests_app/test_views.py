from django.test import TestCase
from stories.views import ContactCreateView
from django.urls import reverse_lazy
from stories.forms import ContactForm
from stories.models import Contact
from django.conf import settings


class TestContactCreateView(TestCase):
    def setUp(self):
        self.contact_url = f'/{settings.LANGUAGE_CODE}/contact/'
        self.url = reverse_lazy('stories:contact')
        self.view = ContactCreateView()
        self.valid_data = {
            'name': 'Idris',
            'email': 'idris.sabanli@gmail.com',
            'subject': 'Sayt islemir',
            'message': 'https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django bu unvanda problem var',
        }
        self.invalid_data = {
            'name': 'IdrisIdrisIdrisIdrisIdrisIdrisIdrisIdrisIdris',
            'email': 'idris.sabanli',
            'subject': 'Sayt islemir',
            'message': 'https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django bu unvanda problem var',
        }

    def test_reverse_lazy_method(self):
        self.assertEqual(self.contact_url, self.url)

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_request(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        contact_data = Contact.objects.last()
        self.assertEqual(self.valid_data['name'], contact_data.name)
        self.assertEqual(self.valid_data['email'], contact_data.email)
        self.assertEqual(self.valid_data['message'], contact_data.message)
        self.assertRedirects(response, f'/{settings.LANGUAGE_CODE}/')

    def test_post_invalid_request(self):
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Keçərli e-poçt ünvanı daxil edin.", html=True)
