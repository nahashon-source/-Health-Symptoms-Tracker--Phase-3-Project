# auth.py

USER_DATA = {
    "admin": "password123",
    "user": "mypassword",
    "nashon": "mwendwa"  # Your desired credentials
}

def authenticate_user(username, password):
    """Authenticate user by checking credentials."""
    print(f"Trying to authenticate '{username}' with password '{password}'")  # Debug line
    if username in USER_DATA and USER_DATA[username] == password:
        return True
    return False
