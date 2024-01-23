from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(student)
admin.site.register(subjects)

class MarksAdminDisplay(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(subject_marks, MarksAdminDisplay)

class RanksAdminDisplay(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks',  'date_of_report']
    ordering = ['student_rank']

    def total_marks(self, obj):
        marks = subject_marks.objects.all()
        marks = marks.filter(student = obj.student)
        total = marks.aggregate(mark = Sum('marks'))
        return total['mark']

admin.site.register(Reportcard, RanksAdminDisplay)