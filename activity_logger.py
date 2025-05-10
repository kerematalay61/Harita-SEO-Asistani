"""
Kullanıcı aktivitelerini detaylı şekilde logs/activity_log.txt dosyasına kaydeder.
"""
import datetime

def log_activity(user, action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] Kullanıcı: {user} → İşlem: {action}\n"
    with open("logs/activity_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_line)
    print(log_line.strip())
