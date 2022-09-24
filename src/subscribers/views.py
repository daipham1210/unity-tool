from .models import Subscriber, SubscriberStatus
import datetime
from django.shortcuts import render

def dashboard(request):
    today = datetime.date.today()
    subscribers = Subscriber.objects.filter(created_at__year=today.year,
                                            created_at__month=today.month).order_by('-id')
    total = Subscriber.objects.all().count()
    count_unsubscribed = Subscriber.objects.filter(status=SubscriberStatus.UNSUBSCRIBED).count()
    context = dict(
        month_header=today.strftime("%B, %Y"),
        subscribers=subscribers,
        total=total,
        count_this_month=subscribers.count(),
        count_unsubscribed=count_unsubscribed,
    )
    return render(request, "dashboard.html", context)