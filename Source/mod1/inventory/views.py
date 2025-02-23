
from django.shortcuts import render, redirect
from .models import ExamSchedule
from .forms import ExamScheduleForm

def dashboard(request):
    schedules = ExamSchedule.objects.all()
    total_tasks = schedules.count()
    completed_tasks = schedules.filter(completed=True).count()
    progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    return render(request, 'dashboard.html', {'schedules': schedules, 'progress': progress})

def schedule_page(request):
    if request.method == "POST":
        form = ExamScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExamScheduleForm()
    
    schedules = ExamSchedule.objects.all()
    return render(request, 'schedule.html', {'form': form, 'schedules': schedules})

def update_completion(request, schedule_id):
    schedule = ExamSchedule.objects.get(id=schedule_id)
    schedule.completed = not schedule.completed
    schedule.save()
    return redirect('dashboard')
