"""
Kullanıcı arayüzü temalarını yönetir.
"""
themes = {
    "light": {
        "background": "#ffffff",
        "text": "#000000",
        "accent": "#1976d2"
    },
    "dark": {
        "background": "#121212",
        "text": "#ffffff",
        "accent": "#bb86fc"
    },
    "blue": {
        "background": "#e3f2fd",
        "text": "#0d47a1",
        "accent": "#2196f3"
    }
}

def get_theme(name="light"):
    return themes.get(name, themes["light"])
theme = get_theme("dark")
bg_color = theme["background"]
