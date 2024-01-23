from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q , Sum # Q is used for using or
# Create your views here.

def get_students(request):
    queryset = student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search) |
            Q(student_address__icontains = search)
            )

    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "students.html", context={"queryset": page_obj})

def see_marks(request, student_id):
    queryset = subject_marks.objects.all()
    queryset = queryset.filter(student__student_id__student_id = student_id)
    total = queryset.aggregate(total_marks = Sum('marks'))
    rank = Reportcard.objects.all()
    rank = rank.filter(student__student_id__student_id = student_id)

    context = {'queryset': queryset , 'total': total, 'rank': rank }
    return render(request, "see_marks.html", context)