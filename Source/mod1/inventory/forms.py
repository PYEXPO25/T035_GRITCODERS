from django import forms
from .models import ExamSchedule

class ExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ['subject', 'time_slot', 'completed']
