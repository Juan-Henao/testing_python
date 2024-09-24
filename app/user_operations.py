users_db = []

def add_user(user: dict):
    if any(u['email'] == user['email'] for u in users_db):
        raise ValueError("User already exists")
    users_db.append(user)

def get_user_by_email(email: str) -> dict:
    return next((u for u in users_db if u['email'] == email), None)

def delete_user(email: str):
    global users_db
    users_db = [u for u in users_db if u['email'] != email]

def list_users() -> list:
    return users_db

def update_user(email: str, new_data: dict):
    user = get_user_by_email(email)
    if not user:
        raise ValueError("User not found")
    user.update(new_data)
