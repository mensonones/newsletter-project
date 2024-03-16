from django.urls import path, include

from rest_framework.routers import DefaultRouter

from newsletter_app import views

router = DefaultRouter()
router.register(r'subscribers', views.SubscriberViewSet)
router.register(r'newsletters', views.NewsletterViewSet)

urlpatterns = [
    path('', include(router.urls))
]