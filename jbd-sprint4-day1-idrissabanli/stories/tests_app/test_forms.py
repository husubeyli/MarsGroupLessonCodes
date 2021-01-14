from django.test import TestCase
from stories.forms import ContactForm


class TestContactForm(TestCase):

    def setUp(self) -> None:
        self.valid_data = {
            'name': 'Idris',
            'email': 'email@gmail.com',
            'subject': 'subject',
            'message': 'https://realpython.com/testing-in-django-part-1-best-practices-and-examples/ sehifesi islemir'
        }

        self.invalid_data1 = {
            'name': 'Idris'
        }

        self.invalid_data2 = {
            'name': 'Idris Idris Idris Idris Idris Idris Idris Idris Idris Idris '
                    'Idris Idris Idris Idris Idris Idris Idris Idris'
                    'Idris Idris Idris Idris Idris Idris Idris Idris Idris'
                    ' Idris Idris Idris Idris Idris Idris Idris Idris Idris'
                    'Idris Idris Idris Idris Idris Idris Idris Idris IdrisIdris'
                    'Idris Idris Idris Idris Idris Idris Idris Idris',
            'email': 'emailosdhfsdf',
            'subject': 'subject',
            'message': 'https://realpython.com/testing-in-django-part-1-best-practices-and-examples/ sehifesi islemir'
        }

    def test_valid_data(self):
        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data1(self):
        form = ContactForm(data=self.invalid_data1)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('email', form.errors.keys())
        self.assertIn('subject', form.errors.keys())
        self.assertIn('message', form.errors.keys())
        self.assertIn('Bu sahə tələb edilir.', form.errors['email'])
        self.assertIn('Bu sahə tələb edilir.', form.errors['subject'])
        self.assertIn('Bu sahə tələb edilir.', form.errors['message'])

    def test_invalid_data2(self):
        form = ContactForm(data=self.invalid_data2)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('email', form.errors.keys())
        self.assertIn('name', form.errors.keys())
        self.assertIn('Keçərli e-poçt ünvanı daxil edin.', form.errors['email'])
        self.assertIn('Bu dəyərin ən çox 50 simvol olduğuna əmin olun (319 var)', form.errors['name'])

    def tearDown(self) -> None:
        del self.valid_data
        del self.invalid_data1
        del self.invalid_data2


