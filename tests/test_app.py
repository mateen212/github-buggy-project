import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from app import get_user, login, delete_user
from calculator import (
    calculate_average,
    calculate_percentage,
    find_maximum
)


def test_get_user():

    assert get_user(1)["username"] == "mateen"


def test_invalid_login():

    assert login("mateen", "wrongpassword") is False


def test_valid_login():

    assert login("mateen", "12345") is True


def test_average():

    assert calculate_average([10, 20, 30]) == 20


def test_percentage():

    assert calculate_percentage(50, 100) == 50


def test_find_maximum():

    assert find_maximum([10, 20, 30]) == 30


def test_delete_nonexistent_user():

    assert delete_user(100) == "User not found"