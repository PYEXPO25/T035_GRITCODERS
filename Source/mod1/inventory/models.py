from django.db import models

class ExamSchedule(models.Model):
    subject = models.CharField(max_length=100)
    time_slot = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} - {self.time_slot} ({'Completed' if self.completed else 'Incomplete'})"