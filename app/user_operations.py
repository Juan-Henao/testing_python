""" asd """
users_db = []


def add_user(user: dict):
    """ asd """

    if any(u['email'] == user['email'] for u in users_db):
        raise ValueError("User already exists")
    users_db.append(user)


def get_user_by_email(email: str) -> dict:
    """ asd """

    return next((u for u in users_db if u['email'] == email), None)


def delete_user(email: str):
    """ asd """
    return [u for u in users_db if u['email'] != email]


def list_users() -> list:
    """ asd """

    return users_db


def update_user(email: str, new_data: dict):
    """ asd """

    user = get_user_by_email(email)
    if not user:
        raise ValueError("User not found")
    user.update(new_data)
