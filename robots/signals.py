from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.service import Send_Email_Notification
from .models import Robot


@receiver(post_save, sender=Robot)
def new_robot_handler(instance, *args, **kwargs):
    Send_Email_Notification().send_email(instance)
