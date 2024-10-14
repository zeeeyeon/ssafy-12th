from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    participants = models.ManyToManyField('Participant', through='Attendance')

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)
    num_of_participants = models.IntegerField()
    events = models.ManyToManyField('Event', through='Attendance')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    check_in = models.TimeField()
    check_out = models.TimeField()
    total_fee = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.participant} - {self.event}'

    def total_price(self):
        return self.event.price * self.participant.num_of_participants

