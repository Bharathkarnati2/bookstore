import pytest
from httpx import AsyncClient
from urllib3 import request

from .conftest import setup, base_url


@pytest.mark.asyncio
class Test:
    @pytest.fixture(autouse=True)
    def set_up_method(self,setup,base_url):
        self.setup = setup
        self.base_url = base_url

    @pytest.mark.parametrize("sample_val", [{
          "id": 9,
          "name": "DS",
          "author": "DS-admin",
          "published_year": 1960,
          "book_summary": "Coding"
        },
    ])

    async def test_insert_book(self,sample_val):
        async with AsyncClient(base_url=self.base_url) as client:
            print(self.base_url , "url")
            data = sample_val
            response = await client.post("/books/",json = data, headers={"Authorization": f"Bearer {self.setup}"})

            assert response.status_code == 200
            print(response.json())

    async def test_get_book_by_id(self):
        """Test retrieving a book by ID using the mocked DB."""
        async with AsyncClient(base_url=self.base_url) as client:
            #resp = await client.get("/book/123")
            response = await client.get(
                "/books/2",
                headers={"Authorization": f"Bearer {self.setup}"},
            )
            assert response.status_code == 200
            print(response.json())



    async def test_update_book(self):
        id_val = 4
        async with AsyncClient(base_url=self.base_url) as client:
            data = {
                      "id": 4,
                      "name": "C",
                      "author": "C-admin",
                      "published_year": 1960,
                      "book_summary": "Coding"
                    }

            response = await client.put(f"/books/{id_val}", json=data, headers={"Authorization": f"Bearer {self.setup}"})

            assert response.status_code == 200
            print(response.json())


    async def test_get_all(self):
        async with AsyncClient(base_url=self.base_url) as client:
            response = await client.get(
                "/books/",
                headers={"Authorization": f"Bearer {self.setup}"},
            )
            assert response.status_code == 200
            print(response.json())


    async def test_delete_book(self):
        del_id = 9
        async with AsyncClient(base_url=self.base_url) as client:

            response = await client.delete(f"/books/{del_id}", headers={"Authorization": f"Bearer {self.setup}"})

            assert response.status_code == 200
            print(response.json())

