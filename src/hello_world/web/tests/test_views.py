"""
Tests for web views.

Following TDD approach with descriptive test names and pytest fixtures.
"""

import pytest
from django.test import RequestFactory
from django.test.client import Client


@pytest.fixture
def request_factory() -> RequestFactory:
    """Provide a Django RequestFactory for testing."""
    return RequestFactory()


@pytest.fixture
def client() -> Client:
    """Provide a Django test client."""
    return Client()


@pytest.mark.django_db
def test_hello_world_view_returns_successful_response(client: Client) -> None:
    """Test that hello world view returns 200 status code."""
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_hello_world_view_contains_hello_world_message(client: Client) -> None:
    """Test that hello world view contains expected message in response."""
    response = client.get("/")
    assert b"Hello World" in response.content


@pytest.mark.django_db
def test_hello_world_view_contains_description(client: Client) -> None:
    """Test that hello world view contains description text."""
    response = client.get("/")
    assert b"A lightweight Django application" in response.content


@pytest.mark.django_db
def test_hello_world_view_uses_correct_template(client: Client) -> None:
    """Test that hello world view uses the correct template."""
    response = client.get("/")
    assert "web/hello.html" in [t.name for t in response.templates]
