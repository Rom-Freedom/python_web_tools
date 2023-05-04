from django.test import TestCase

# Create your tests here.

class PythonTools(TestCase):

    def test_index(self):
        response = self.client.get('/basicPythonTools/')
        self.assertEqual(response.status_code, 200)

    def test_core(self):
        response = self.client.get('/basicPythonTools/core')
        self.assertEqual(response.status_code, 200)
        self.assertIn('В этом разделе представлена вся необходимые ссылки для изучения языка Python',
                      response.content.decode())

    def test_core_redirect(self):
        response = self.client.get('/basicPythonTools/1')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/basicPythonTools/core')