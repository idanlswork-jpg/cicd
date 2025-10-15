# tests/test_main.py
from main import add_user, get_user_count, clear_users
import pytest


@pytest.fixture(autouse=True)
def reset_users():
    """Automatically clear users before each test"""
    clear_users()
    yield
    clear_users()


def test_add_user_increases_count():
    """Verify that adding a user increases the count by 1"""
    start = get_user_count()
    add_user("idan")
    assert get_user_count() == start + 1


def test_add_user_rejects_empty_name():
    """Verify that empty string raises ValueError"""
    try:
        add_user("")
        assert False, "Empty name should raise ValueError"
    except ValueError:
        assert True
