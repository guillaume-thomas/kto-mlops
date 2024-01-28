import unittest

from fastapi.testclient import TestClient
from cats_dogs_other.api.src import index

client = TestClient(index.app)


class TestIndex(unittest.TestCase):
    def test_health(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})

    def test_upload(self):
        with open("./cats_dogs_other/api/src/tests/resources/cat.png", "rb") as file:
            response = client.post("/upload", files={"file": ("filename", file, "image/png")})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['prediction'], 'Cat')
