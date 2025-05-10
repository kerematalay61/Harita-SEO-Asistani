users = {
    "admin@haritaseoasistani.com": {
        "password": "$2b$12$ExampleHashedPass",
        "role": "admin",
        "verified": True
    }
}

def get_user(email):
    return users.get(email)

def add_user(email, password, role="user"):
    ...

def verify_user(email):
    ...
