from django.db import models
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)  # Add deadline field
    completed = models.BooleanField(default=False)  # Add completed field

    def __str__(self):
        return self.title

    def is_deadline_passed(self):
        # Check if the deadline has passed
        if self.deadline:
            return timezone.now() > self.deadline
        return False
    