"""
Yönetici tarafından sistem ayarlarının kontrol edilmesini sağlar (örnek: pin limiti).
"""
settings = {
    "default_pin_limit": 100,
    "default_comment_limit": 50,
    "language": "tr",
    "theme": "light"
}

def update_setting(key, value):
    if key in settings:
        settings[key] = value

def get_setting(key):
    return settings.get(key)
