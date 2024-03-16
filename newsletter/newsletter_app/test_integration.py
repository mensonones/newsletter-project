from rest_framework.test import APITestCase, APIClient


class SubscriberViewSetTestCase(APITestCase):
    def test_create_subscriber(self):
        self.client = APIClient()
        response = self.client.post('/api/subscribers/', {'email': 'test@mail.com'})
        self.assertEqual(response.status_code, 201)

    def get_subscribers(self):
        self.client = APIClient()
        response = self.client.get('/api/subscribers/')
        self.assertEqual(response.status_code, 200)


class NewsletterViewSetTestCase(APITestCase):
    def test_create_newsletter(self):
        self.client = APIClient()
        subject = 'Test subject'
        body = 'Test body'
        response = self.client.post('/api/newsletters/', {'subject': subject, 'body': body})
        self.assertEqual(response.status_code, 201)

    def get_newsletters(self):
        self.client = APIClient()
        response = self.client.get('/api/newsletters/')
        self.assertEqual(response.status_code, 200)
