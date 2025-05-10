users = {
    "admin@haritaseoasistani.com": {
        "password": "Kerem@2025!",
        "role": "admin"
    },
    "uye@example.com": {
        "password": "uye123",
        "role": "user"
    }
}

def authenticate(email, password):
    if email in users and users[email]['password'] == password:
        return users[email]['role']
    return None
