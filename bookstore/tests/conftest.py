import os
from unittest.mock import AsyncMock, MagicMock
import pytest
from httpx import AsyncClient

import pytest
import configparser



@pytest.fixture
def mock_db():
    """Fixture to create a mock MongoDB collection."""
    mock_collection = MagicMock()
    return mock_collection


BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")


@pytest.fixture(scope="session")
def base_url():
    """Fixture to return the base URL from the ini file."""
    return BASE_URL


@pytest.fixture
async def setup(base_url):
    """Fixture to setup test client and login data."""
    async with AsyncClient(base_url=base_url) as client:
        data = {
              "email": "string",
              "password": "string"
        }
        response = await client.post("/login", json=data)
        if response.status_code == 200:
            resp_json = response.json()
            access_token = resp_json["access_token"]
            yield  access_token
        elif "Incorrect email or password" in response.text:
            response_signup = await client.post("/signup", json=data)
            if response_signup.status_code ==200:
                response = await client.post("/login", json=data)
                assert response.status_code == 200
                resp_json = response.json()
                access_token = resp_json["access_token"]
                yield  access_token



