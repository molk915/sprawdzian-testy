import pytest
from app.logic import UserManager

def test_add_user():
    manager = UserManager()
    user = manager.add_user("Jan", "Kowalski", 1985, "user")
    assert user.id == 1
    assert user.firstName == "Jan"
    assert user.lastName == "Kowalski"
    assert user.birthYear == 1985
    assert user.group == "user"

def test_get_user():
    manager = UserManager()
    user = manager.add_user("Jan", "Kowalski", 1985, "user")
    fetched_user = manager.get_user(1)
    assert fetched_user == user


