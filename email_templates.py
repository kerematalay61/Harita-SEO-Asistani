"""
E-posta içerikleri için şablonlar sağlar (doğrulama, uyarı, bildirim).
"""
def get_template(template_name, **kwargs):
    templates = {
        "verification_code": "Merhaba,\n\nGiriş için doğrulama kodunuz: {code}\n\nHarita SEO Asistanı Ekibi",
        "reset_notice": "Sayın {name},\n\nHesap haklarınız yönetici tarafından sıfırlanmıştır.\n\nHarita SEO Asistanı",
        "welcome": "{name} hoş geldiniz! Sisteme başarıyla kayıt oldunuz."
    }
    template = templates.get(template_name, "")
    return template.format(**kwargs)
