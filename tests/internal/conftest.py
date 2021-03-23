from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

