from datetime import datetime
from django.utils import timezone
from django.core.mail import send_mail
from django_q.tasks import schedule, async_task
from inTime.models import Task

def check_overdue_tasks():
    overdue_tasks = Task.objects.filter(due_time__lte=timezone.now(), completed=False)
    for task in overdue_tasks:
        subject = "Task Overdue"
        message = f"Your task '{task.title}' is overdue."
        async_task(send_mail, subject, message, 'from@example.com', [task.user.email], fail_silently=False)

schedule('check_overdue_tasks', minutes=1, repeats=-1)
