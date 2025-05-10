"""
Üyelerin işlem haklarını (yorum/pinleme) kontrol eden sistem.
"""
permissions = {}

def set_user_limits(email, max_comments, max_pins):
    permissions[email] = {
        "max_comments": max_comments,
        "max_pins": max_pins,
        "used_comments": 0,
        "used_pins": 0
    }

def can_comment(email):
    user = permissions.get(email)
    return user and user['used_comments'] < user['max_comments']

def can_pin(email):
    user = permissions.get(email)
    return user and user['used_pins'] < user['max_pins']

def record_comment(email):
    if can_comment(email):
        permissions[email]['used_comments'] += 1

def record_pin(email):
    if can_pin(email):
        permissions[email]['used_pins'] += 1
