""" Demonstrating Flask, using APScheduler. """

from apscheduler.schedulers.background import BackgroundScheduler
from app import app
from app.tasks import send_tweet

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(send_tweet, 'cron', hour=10)
scheduler.start()

if __name__ == "__main__":
    app.run()
