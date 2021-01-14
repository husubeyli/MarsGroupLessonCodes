from django.test import TestCase
from stories.models import Contact


class TestContact(TestCase):

    def setUp(self) -> None:
        self.valid_data = {
            'name': 'Idris',
            'email': 'email@gmail.com',
            'subject': 'subject',
            'message': 'https://realpython.com/testing-in-django-part-1-best-practices-and-examples/ sehifesi islemir'
        }
        self.contact = Contact.objects.create(**self.valid_data)

        self.valid_data2 = {
            'name': 'Nizami',
            'email': 'nizami@gmail.com',
            'subject': 'subject',
            'message': 'https://realpython.com/testing-in-django-part-1-best-practices-and-examples/ sehifesi islemir'
        }
        self.contact2 = Contact.objects.create(**self.valid_data2)

    def test_created_data(self):
        contact1 = Contact.objects.last()

        self.assertEqual(contact1.name, self.valid_data['name'])
        self.assertEqual(contact1.email, self.valid_data['email'])
        self.assertEqual(contact1.subject, self.valid_data['subject'])
        self.assertEqual(contact1.message, self.valid_data['message'])

        contact2 = Contact.objects.first()

        self.assertEqual(contact2.name, self.valid_data2['name'])
        self.assertEqual(contact2.email, self.valid_data2['email'])
        self.assertEqual(contact2.subject, self.valid_data2['subject'])
        self.assertEqual(contact2.message, self.valid_data2['message'])

    def test_str_method(self):
        self.assertEqual(str(self.contact), self.valid_data['name'])

    def tearDown(self):
        Contact.objects.filter(id__in=[self.contact.id, self.contact2.id]).delete()
