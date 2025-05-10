"""
Program hatalarını yakalayarak logs/error_log.txt dosyasına kayıt eder.
"""
import traceback
import datetime

def log_error(error):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/error_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] HATA: {str(error)}\n")
        log_file.write(traceback.format_exc())
        log_file.write("\n---\n")
    print(f"[!] Hata loglandı: {error}")
try:
    # işlem
except Exception as e:
    log_error(e)
