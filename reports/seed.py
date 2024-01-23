from faker import Faker
fake = Faker()
from .models import *
import random
from django.db.models import Sum

def create_sub_marks(n):
    try:
        student_obj = student.objects.all()
        for stu in student_obj:
            subject = subjects.objects.all()
            for sub in subject:
                subject_marks.objects.create(
                    student = stu,
                    subject = sub,
                    marks = random.randint(0,100),
                )

    except Exception as e:
        print(e)

def seed_stu(n=10):

    try:
        for _ in range(0, n):
            department_obj = Department.objects.all()
            d_index = random.randint(0, len(department_obj)-1)
            department = department_obj[d_index]
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student.objects.create(
            department = department,
            student_id = student_id_obj,
            student_name = student_name,
            student_email = student_email,
            student_age = student_age,
            student_address = student_address,
            )

    except Exception as e:
        print(e)   

def generate_report_card():
    ranks = student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    
    i =1
    for rank  in ranks:
        Reportcard.objects.create(
            student = rank,
            student_rank = i
        )
        i = i + 1