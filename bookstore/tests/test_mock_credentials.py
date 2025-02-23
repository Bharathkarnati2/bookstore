import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .conftest import *
from bookstore.main import *

@pytest.mark.asyncio
async def test_signup(mock_db):
    mock_db.query().filter().first.return_value = None

    # Test input (new user)
    new_user = MagicMock()
    new_user.email = "new_user@example.com"
    new_user.password = "new_password"

    # Mocking DB functions
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    # Call the function
    response = await create_user_signup(new_user, mock_db)

    # Assertions
    assert response == {"message": "User created successfully"}


@pytest.mark.asyncio
async def test_login(mock_db):
    hashed_password = pwd_context.hash("pwd")

    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.email = "user_b"
    mock_user.password = hashed_password

    mock_db.query().filter().first.return_value = mock_user

    login_data = MagicMock()
    login_data.email = "user_b"
    login_data.password = "pwd"

    # Call the login function
    response = await login_for_access_token(login_data, mock_db)

    assert response is not None