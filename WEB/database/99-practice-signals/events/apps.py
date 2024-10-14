from django.apps import AppConfig
from django.core.signals import request_finished
from django.db.models.signals import post_save

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self) -> None:
        from .models import Attendance
        from .signals import calculate_post_save

        # from .models import Attendance
        # post_save.connect('calculate_post_save', sender='Attendance')
        # return super().ready()

        post_save.connect(calculate_post_save, sender=Attendance)
        request_finished.connect(calculate_post_save)

        return super().ready()