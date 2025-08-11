"""
URL routing for web module.

Maps URLs to views following Django conventions.
"""

from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.hello_world, name="hello_world"),
]
