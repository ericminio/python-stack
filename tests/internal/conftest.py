from app import app, db as database
from flask_sqlalchemy import SQLAlchemy
import pytest

@pytest.fixture
def client():
    return app.test_client()

@pytest.fixture
def clean_db():
    database.engine.execute('truncate table foi_user')
    database.engine.execute('alter sequence foi_user_id_seq restart with 1')

@pytest.fixture
def db(clean_db):
    return database


