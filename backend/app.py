from routes import app
from routes.worker import celery_init_app
from celery.schedules import crontab # type: ignore
from routes.tasks import *

celery_app = celery_init_app(app)

@celery_app.on_after_configure.connect
def send_email(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=20, minute=31, day_of_month=25),
        monthly_reminder.s(),
    )
    # sender.add_periodic_task(
    #     crontab(hour=20, minute=14),
    #     monthly_reminder.s(),
    # )

if __name__ == '__main__':
    app.run(debug=True)