from django.urls import path
from . import views

urlpatterns = [
    path("currencies", views.TestView.as_view())
]
