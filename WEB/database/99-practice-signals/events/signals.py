from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Attendance

@receiver(post_save, sender=Attendance)
def calculate_post_save(sender, instance, created, **kwargs):
    if created:
        event = instance.event
        participant = instance.participant
        instance.total_fee = event.price * participant.num_of_participants
        instance.save()