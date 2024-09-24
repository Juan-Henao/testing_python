from app import main
from test.test_main import client


def test_create_user_with_mock(mocker):
    # Arrange
    mocker.patch('app.main.users_db', [])
    new_user = {"id": 3, "name": "Mocked User", "email": "mock@example.com"}

    # Act
    response = client.post("/users/", json=new_user)

    # Assert
    assert response.status_code == 200
    assert response.json() == new_user
    assert len(main.users_db) == 1

