"""
Basit kullanıcı oturumlarını saklamak ve kontrol etmek için oturum yöneticisi.
"""
sessions = {}

def create_session(email):
    sessions[email] = True

def destroy_session(email):
    if email in sessions:
        del sessions[email]

def is_logged_in(email):
    return sessions.get(email, False)
