import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users_empty(client):
    """Test /users endpoint when no users are present"""
    rv = client.get('/users')
    assert rv.status_code == 200
    assert rv.json == []

def test_create_user(client):
    """Test creating a user"""
    rv = client.post('/users', json={
        "firstName": "Jan",
        "lastName": "Kowalski",
        "birthYear": 1985,
        "group": "user"
    })
    assert rv.status_code == 201
    json_data = rv.json
    assert json_data['firstName'] == "Jan"
    assert json_data['age'] == 2024 - 1985  # Assuming current year is 2024
