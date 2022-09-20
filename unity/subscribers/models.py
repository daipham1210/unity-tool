from django.utils.translation import gettext_lazy as _
from django.db import models

class SubscriberStatus:
    SUBSCRIBED = 1
    UNSUBSCRIBED = 2

    @classmethod
    def to_text(cls, val):
        if val == cls.SUBSCRIBED:
            return "Subscribed"
        elif val == cls.UNSUBSCRIBED:
            return "Unsubscribed"


SUBSCRIBER_STATUSES = [
    (SubscriberStatus.SUBSCRIBED, "Subscribed"),
    (SubscriberStatus.UNSUBSCRIBED, "Unsubscribed"),
]


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, default="", db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(default=SubscriberStatus.SUBSCRIBED, choices=SUBSCRIBER_STATUSES)

    @property
    def status_label(self):
        return SubscriberStatus.to_text(self.status)
