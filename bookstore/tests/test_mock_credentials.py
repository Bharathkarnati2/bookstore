import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from .conftest import *
from bookstore.main import *

@pytest.mark.asyncio
async def test_signup(mock_db):
    data = UserCredentials(
        id=1,
        email='user_b',
        password='pwd'
    )
    with pytest.raises(HTTPException) as exc_info:
        await create_user_signup(data, mock_db)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Email already registered"


# @pytest.mark.asyncio
# async def test_login(mock_db):
#     data = UserCredentials(
#         id=1,
#         email='user_b',
#         password='pwd'
#     )
#
#     response = await login_for_access_token(data,mock_db)