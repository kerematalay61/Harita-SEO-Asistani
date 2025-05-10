"""
Kullanıcı tercihine göre uygulama dilini yöneten çoklu dil modülü.
"""
languages = {
    "tr": {
        "welcome": "Hoş geldiniz",
        "login": "Giriş Yap",
        "logout": "Çıkış Yap",
        "panel": "Yönetim Paneli"
    },
    "en": {
        "welcome": "Welcome",
        "login": "Login",
        "logout": "Logout",
        "panel": "Admin Panel"
    },
    "ar": {
        "welcome": "أهلا بك",
        "login": "تسجيل الدخول",
        "logout": "تسجيل الخروج",
        "panel": "لوحة التحكم"
    }
}

def get_text(key, lang="tr"):
    return languages.get(lang, languages["tr"]).get(key, key)
