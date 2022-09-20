from django.urls import path
from . import apiviews, views

urlpatterns = [
    path('api/subscribers', apiviews.SubscriberListView.as_view()),
    path('subscribers/dashboard', views.dashboard, name='dashboard'),
]
