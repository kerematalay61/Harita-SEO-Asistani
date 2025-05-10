"""
Her kullanıcı için pinleme sayısını takip eden ve artıran sayaç sistemidir.
"""
pin_counts = {}

def increment_pin(user_email):
    if user_email not in pin_counts:
        pin_counts[user_email] = 0
    pin_counts[user_email] += 1
    return pin_counts[user_email]

def get_pin_count(user_email):
    return pin_counts.get(user_email, 0)
