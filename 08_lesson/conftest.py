import pytest

@pytest.fixture
def base_url():
    return "https://ru.yougile.com/api-v2"

@pytest.fixture
def auth_headers():
    # Заменить токен
    token = "your_auth_token_here"
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }