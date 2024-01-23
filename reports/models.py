from django.db import models

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

class student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE, null=True, blank=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class subjects(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name


class subject_marks(models.Model):
    student = models.ForeignKey(student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE)
    marks = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student', 'subject']

class Reportcard(models.Model):
    student = models.ForeignKey(student, related_name="studentreportcard", on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report = models.DateField(auto_now_add = True) # in order to set date automatically we use auto_now_add =  true

    class Meta:
        unique_together = ['student_rank', 'date_of_report']