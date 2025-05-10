"""
Yönetici işlemleri: kullanıcı silme, işlem sayaçlarını sıfırlama.
"""
from pin_tracker import pin_counts
from permission_control import permissions

def delete_user(email):
    if email in permissions:
        del permissions[email]
    if email in pin_counts:
        del pin_counts[email]
    print(f"Kullanıcı silindi: {email}")

def reset_user_usage(email):
    if email in permissions:
        permissions[email]["used_comments"] = 0
        permissions[email]["used_pins"] = 0
        print(f"Kullanıcı hakları sıfırlandı: {email}")
