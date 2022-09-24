
import datetime
from django.core.management import BaseCommand

from subscribers.models import Subscriber


class Command(BaseCommand):
    help = "Send Subscriber Report to Admins"

    def handle(self, *args, **options):
        today = datetime.date.today()
        count_subscribers = Subscriber.objects.filter(created_at__year=today.year,
                                                    created_at__month=today.month).count()
        self.stdout.write(f"There are {count_subscribers} signed up emails this month!")