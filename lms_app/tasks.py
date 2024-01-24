from celery import shared_task
from lms_app.models import Course
from datetime import datetime, timedelta
from lms_app.services import mailing_util


@shared_task
def send_updates(inst):
    course = Course.objects.get(pk=inst)
    # now = datetime.now()
    # no_spam_time = now - timedelta(hours=4)
    # if course.updated_at.timestamp() > no_spam_time.timestamp():
    #     return
    # else:
    subscribers = course.subscribe.all()
    subscribers_list = [subscribe.user for subscribe in subscribers]
    mailing_util(
        subject='Course were updated!',
        message=f'You get update in {course}!',
        recipient_list=subscribers_list,
    )
