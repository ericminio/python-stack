from app import app, db as database
from flask_sqlalchemy import SQLAlchemy
import pytest

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def db():
    return database


