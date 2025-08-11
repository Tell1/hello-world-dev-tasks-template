"""
Hello World view module.

Contains the main view for displaying "Hello World" message.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hello_world(request: HttpRequest) -> HttpResponse:
    """
    Display Hello World message.

    Simple view that renders a "Hello World" message.

    Args:
        request: Django HTTP request object

    Returns:
        HTTP response with rendered Hello World template

    Example:
        >>> from django.test import RequestFactory
        >>> factory = RequestFactory()
        >>> request = factory.get('/')
        >>> response = hello_world(request)
        >>> response.status_code
        200
    """
    context = {"message": "Hello World", "description": "A lightweight Django application"}
    return render(request, "web/hello.html", context)
