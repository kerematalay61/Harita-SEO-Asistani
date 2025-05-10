"""
Geçici klasörlerde biriken gereksiz dosyaları temizler.
"""
import os
import time

def clean_directory(path, max_age_seconds=86400):
    now = time.time()
    if not os.path.exists(path):
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            file_age = now - os.path.getmtime(file_path)
            if file_age > max_age_seconds:
                os.remove(file_path)
                print(f"Silindi: {file_path}")
clean_directory("static/uploads", 3600)  # 1 saatten eski tüm dosyaları sil
