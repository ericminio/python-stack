from app import app
from flask_sqlalchemy import SQLAlchemy
import pytest

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def connectionString():
    return 'postgresql://dev:dev@host.docker.internal:2345/exploration'

@pytest.fixture
def db(connectionString):
    app.config['SQLALCHEMY_DATABASE_URI'] = connectionString
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return db


