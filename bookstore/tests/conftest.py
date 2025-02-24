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




def get_config():
    """Reads pytest.ini manually and extracts the URL."""
    config_path = os.path.join(os.path.dirname(__file__), "pytest.ini")
    config = configparser.ConfigParser()

    if os.path.exists(config_path):
        config.read(config_path)
        url = config.get("URL", "url")
        return url
    #return "http://127.0.0.1:8000"  # Fallback URL





@pytest.fixture(scope="session")
def base_url():
    """Fixture to return the base URL from the ini file."""
    return get_config()


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



