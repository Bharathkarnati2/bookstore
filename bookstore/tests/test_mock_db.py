import sys

import pytest
import os
from unittest.mock import AsyncMock, MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bookstore.bookmgmt import create_book, get_all_books, get_book_by_id, update_book, delete_book
from bookstore.database import Book
from .conftest import *


# from app.models import Book

@pytest.fixture
def sample_book():
    """Fixture to provide a sample book document."""
    return Book(
    id=1,
    author="Mock Author",
    published_year=2024
)

@pytest.mark.asyncio
async def test_create_book(mock_db, sample_book):
    """Test book creation."""

    response = await create_book(sample_book, mock_db)

    assert response.author == "Mock Author"


@pytest.mark.asyncio
async def test_get_all_books(mock_db,sample_book):
    """Test retrieving all books from SQLAlchemy."""
    mock_db.query.return_value.all.return_value = [
        Book(id=1, title="Book 1", author="Author 1", published_year=2023),
        Book(id=2, title="Book 2", author="Author 2", published_year=2024),
    ]

    response = await get_all_books(mock_db)

    assert len(response) == 2
    assert response[0].author == "Author 1"
    assert response[1].author == "Author 2"


@pytest.mark.asyncio
async def test_get_book_by_id(mock_db):
    """Test retrieving a book by ID."""

    response = await get_book_by_id(1, mock_db)

    assert response is not None


@pytest.mark.asyncio
async def test_update_book(mock_db, sample_book):
    """Test updating a book."""
    mock_db.find_one.return_value = sample_book
    mock_db.update_one.return_value.modified_count = 1

    update_data =  Book(id = 1, author="Updated Book")
    response = await update_book(1, update_data, mock_db)

    assert response.author == "Updated Book"
    assert response.id == 1

@pytest.mark.asyncio
async def test_delete_book(mock_db):
    """Test deleting a book."""
    mock_db.find_one.return_value = {"_id": 1}
    mock_db.delete_one.return_value.deleted_count = 1

    response = await delete_book(1, mock_db)

    assert response == {"message": "Book deleted successfully"}

