from django.test import TestCase, Client
# Create your tests here.


class SimpleTest(TestCase):
    fixtures = ['fixture.json']

    def setUp(self):
        # fixtures = ['fixture.json']
        # Every test needs a client.
        self.client = Client()

    def test_redirect(self):
        # Issue a GET request.
        response = self.client.get('login')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 302)
        print (response.context)

    def test_event_list(self):
        # Issue a GET request.
        response = self.client.get('/events/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered context contains 4 events.
        self.assertEqual(len(response.context['event_list']), 4)