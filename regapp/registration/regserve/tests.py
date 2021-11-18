from django.test import TestCase, Client

class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get("/regserve")
        print(f"Inside hello world test, response is {response}.")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Response from Django backend.")