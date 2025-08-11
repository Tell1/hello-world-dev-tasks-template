"""
Main URL configuration for hello_world project.

Simple URL routing following KISS principles.
"""

from django.urls import include, path

urlpatterns = [
    path("", include("hello_world.web.urls")),
]
