import schedule
import time
from ai_comments import generate_comment
from log_writer import write_log

def schedule_comment(keyword, interval=5):
    def job():
        comment = generate_comment(keyword)
        write_log(f"Yorum zamanlandı ve oluşturuldu: {comment}")
        print("Gönderilen yorum:", comment)

    schedule.every(interval).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
# schedule_comment("çamaşır makinesi servisi", 10)
