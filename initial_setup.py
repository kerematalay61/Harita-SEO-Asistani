"""
İlk kurulumda klasörleri ve log dosyalarını otomatik oluşturur.
"""
import os

def ensure_directories():
    folders = ["logs", "static/avatars", "static/uploads"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Klasör kontrol edildi/oluşturuldu: {folder}")

def ensure_log_files():
    files = ["logs/activity_log.txt", "logs/error_log.txt"]
    for file in files:
        if not os.path.exists(file):
            with open(file, "w", encoding="utf-8") as f:
                f.write(f"# {file} log dosyası oluşturuldu\n")
            print(f"Log dosyası oluşturuldu: {file}")

if __name__ == "__main__":
    ensure_directories()
    ensure_log_files()
