from django.shortcuts import render
from rest_framework import viewsets

from newsletter_app.models import Newsletter, Subscriber
from newsletter_app.serializers import NewsletterSerializer, SubscriberSerializer
from rest_framework.response import Response


# Create your views here.
class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class NewsletterViewSet(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
