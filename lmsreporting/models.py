# models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Module(models.Model):
    CATEGORY_CHOICES = [
        ('Core', 'Core'),
        ('Elective', 'Elective'),
    ]

    AVAILABILITY_CHOICES = [
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credit = models.IntegerField()
    category = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    description = models.TextField()
    allowed_courses = models.ManyToManyField('Course')
    registered_students = models.ManyToManyField(User, related_name='registered_modules', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.code})"

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date_of_registration = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Registration: {self.student.user.username} -> {self.module.title}"

    class Meta:
        unique_together = ('student', 'module')

class Issue(models.Model):
    type = models.CharField(max_length=100, choices=[('Hardware', 'Hardware'), ('Software', 'Software')])
    room = models.CharField(max_length=100)
    urgent = models.BooleanField(default=False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='issues', on_delete=models.CASCADE)

 