from django.db import models

# Create your models here.


class Department (models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=300)

    class Meta:
        db_table = 'Department'
        ordering = ['name', ]

    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    name = models.CharField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Course'
        ordering = ['department', ]

    def __str__(self):
        return '{}'.format(self.name)


class Form(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    mail_id = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200)
    materials_provide = models.CharField(max_length=300)

    class Meta:
        db_table = 'Form'

    def __str__(self):
        return '{}'.format(self.name)