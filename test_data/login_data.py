class LoginData:
    valid_user = {
        "username": "Admin",
        "password": "admin123"
    }

    invalid_user = [
        {"username": "Admin", "password": "wrongpass"},
        {"username": "wronguser", "password": "admin123"},
        {"username": "wesas", "password": "admin123"},
        {"username": "aassdda", "password": "112312asd"}
    ]

    invalid_cred = {
        "username": "adadmin",
        "password": "passw"
    }

