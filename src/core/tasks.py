from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)


# @shared_task
# def sample_task():
#     logger.info("The sample task just ran.")

@shared_task
def send_subscriber_report():
    call_command("subscriber_report", )