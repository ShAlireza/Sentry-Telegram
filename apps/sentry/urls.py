from django.urls import path

from . import views

app_name = 'sentry'

urlpatterns = [
    path('webhook', view=views.WebhookAPIView.as_view(), name='webhook')
]
