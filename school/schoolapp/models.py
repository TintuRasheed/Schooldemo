
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


# class Purpose(models.Model):
#     name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class UserInform(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purposechoices=(
        ('S','-------'),
        ('E','Enquiry'),
        ('P','Place Order'),
        ('R','Return')
        
    )
    purpose = models.CharField(max_length=1,default='S',choices=purposechoices)
    materials_provide = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name