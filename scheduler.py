import schedule
import time
import threading

from file_cleaner import clean_directory

def start_scheduler():
    schedule.every().day.at("03:00").do(lambda: clean_directory("static/uploads", 86400))

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_schedule)
    thread.daemon = True
    thread.start()
