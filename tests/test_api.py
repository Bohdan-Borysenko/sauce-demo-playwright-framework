import pytest
import requests
from utils.logger import logger

@pytest.mark.api
def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    assert len(response.json()) > 0
    logger.info("GET users test passed")


@pytest.mark.api
def test_create_post():
    payload = {
        "title": "QA Automation Test",
        "body": "This is a test from Playwright framework",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201
    logger.info("POST create post test passed")