class LoginData:
    valid_user = {
        "username": "Admin",
        "password": "admin123"
    }

    invalid_user = [
        {"username": "Admin", "password": "wrongpass"},
        {"username": "wronguser", "password": "admin123"},
        {"username": "wesas", "password": "admin123"},
        {"username": "Admin", "password": "112312asd"}
    ]
