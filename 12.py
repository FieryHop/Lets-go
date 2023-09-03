
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_register_user(client):
    # Отправляем POST-запрос для регистрации пользователя
    response = client.post("/register", json={"username": "testuser", "password": "testpassword"})

    # Проверяем, что запрос был успешным
    assert response.status_code == 200

    # Проверяем, что в ответе содержится токен доступа
    assert "access_token" in response.json()


@pytest.fixture
def client():
    return TestClient(app)

def test_login_user(client):
    # Отправляем POST-запрос для входа пользователя
    response = client.post("/login", data={"username": "testuser", "password": "testpassword"})

    # Проверяем, что запрос был успешным
    assert response.status_code == 200

    # Проверяем, что в ответе содержится токен доступа
    assert "access_token" in response.json()

@pytest.fixture
def client():
    return TestClient(app)

def test_create_post(client):
    # Отправляем POST-запрос для создания поста
    response = client.post("/posts", json={"title": "Test Post", "content": "This is a test post."})

    # Проверяем, что запрос был успешным
    assert response.status_code == 200

    # Проверяем, что в ответе содержится созданный пост
    assert "title" in response.json()
    assert "content" in response.json()

@pytest.fixture
def client():
    return TestClient(app)

def test_delete_post(client):
    # Отправляем DELETE-запрос для удаления поста с указанным ID
    response = client.delete("/posts/1")

    # Проверяем, что запрос был успешным
    assert response.status_code == 200

    # Проверяем, что в ответе содержится сообщение об успешном удалении
    assert "message" in response.json()
    assert response.json()["message"] == "Post deleted successfully"


@pytest.fixture
def client():
    return TestClient(app)

def test_like_post(client):
    # Отправляем POST-запрос для лайка поста с указанным ID
    response = client.post("/posts/1/like")

    # Проверяем, что запрос был успешным
    assert response.status_code == 200

    # Проверяем, что в ответе содержится сообщение об успешном лайке
    assert "message" in response.json()
    assert response.json()["message"] == "Post liked successfully"



@pytest.fixture
def client():
    return TestClient(app)

def test_dislike_post(client):
    # Отправляем POST-запрос для дизлайка поста с указанным ID
    response = client.post("/posts/1/dislike")

    # Проверяем, что запрос был успешным
    assert response.status_code == 200

    # Проверяем, что в ответе содержится сообщение об успешном дизлайке
    assert "message" in response.json()
    assert response.json()["message"] == "Post disliked successfully"


@pytest.fixture
def client():
    return TestClient(app)

def test_view_post(client):
    # Отправляем GET-запрос для просмотра поста с указанным ID
    response = client.get("/posts/1")

    # Проверяем, что запрос был успешным
    assert response.status_code == 200

    # Проверяем, что в ответе содержится просматриваемый пост
    assert "title" in response.json()
    assert "content" in response.json()

