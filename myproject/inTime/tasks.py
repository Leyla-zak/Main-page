from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Task

@shared_task
def check_overdue_tasks():
    overdue_tasks = Task.objects.filter(due_date__lt=timezone.now(), completed=False)
    for task in overdue_tasks:
        subject = f"Task '{task.title}' is overdue"
        message = render_to_string('tasks/overdue_task_email.html', {'task': task})
        send_mail(
            subject,
            message,
            'from@example.com',
            [task.user.email],
            fail_silently=False,
        )
        print(f"Overdue task '{task.title}' notification sent to {task.user.email}")
