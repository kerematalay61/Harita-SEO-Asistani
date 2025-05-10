"""
UI'da kullanılan sabit metinlerin merkezi yönetimini sağlar.
"""
strings = {
    "tr": {
        "welcome": "Hoş geldiniz!",
        "login_button": "Giriş Yap",
        "logout_button": "Çıkış",
        "dashboard_title": "Yönetim Paneli",
        "invalid_login": "Geçersiz kullanıcı adı veya şifre."
    },
    "en": {
        "welcome": "Welcome!",
        "login_button": "Login",
        "logout_button": "Logout",
        "dashboard_title": "Dashboard",
        "invalid_login": "Invalid username or password."
    },
    "ar": {
        "welcome": "أهلا بك!",
        "login_button": "تسجيل الدخول",
        "logout_button": "تسجيل الخروج",
        "dashboard_title": "لوحة التحكم",
        "invalid_login": "اسم المستخدم أو كلمة المرور غير صحيحة."
    }
}

def ui_text(key, lang="tr"):
    return strings.get(lang, strings["tr"]).get(key, key)
ui_text("welcome", lang="en")
