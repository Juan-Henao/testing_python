from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# Pruebas para el endpoint GET /users/
def test_get_users():
    # Arrange
    expected_users = [
        {"id": 1, "name": "John Doe", "email": "johndoe@example.com"},
        {"id": 2, "name": "Jane Doe", "email": "janedoe@example.com"}
    ]

    # Act
    response = client.get("/users/")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_users


# Pruebas para el endpoint POST /users/
def test_create_user():
    # Arrange
    new_user = {"id": 3, "name": "Alice", "email": "alice@example.com"}

    # Act
    response = client.post("/users/", json=new_user)

    # Assert
    assert response.status_code == 200
    assert response.json() == new_user


def test_create_user_email_already_registered():
    # Arrange
    new_user = {"id": 3, "name": "Alice", "email": "johndoe@example.com"}

    # Act
    response = client.post("/users/", json=new_user)

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}


# Pruebas para el endpoint DELETE /users/{user_id}
def test_delete_user():
    # Arrange
    user_id_to_delete = 1

    # Act
    response = client.delete(f"/users/{user_id_to_delete}")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}


def test_delete_user_not_found():
    # Arrange
    user_id_to_delete = 999  # Usuario inexistente

    # Act
    response = client.delete(f"/users/{user_id_to_delete}")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
