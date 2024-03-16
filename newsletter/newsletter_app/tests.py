from django.test import TestCase

from newsletter_app.models import Subscriber, Newsletter


# Create your tests here.
# unit testing
class SubscriberTest(TestCase):
    def test_create_subscriber(self):
        """
        Test creating a new Subscriber object.
        """
        email = 'test@mail.com'
        subscriber = Subscriber.objects.create(email=email)

        self.assertEqual(subscriber.email, email)


class NewsletterTest(TestCase):
    def test_create_newsletter(self):
        """
        Test creating a new Newsletter object.
        """
        subject = "Test Newsletter Subject"
        body = "This is a test newsletter body."
        newsletter = Newsletter.objects.create(subject=subject, body=body)

        self.assertEqual(newsletter.subject, subject)
        self.assertEqual(newsletter.body, body)
