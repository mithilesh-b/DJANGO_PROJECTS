from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(('IT','Information Technology'),('COMM','Communication'),('INFRA','Infrastructure')))
    added_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    designation = models.CharField(max_length=50, choices=(('mgr','Manager'),('sd','Software developer'),('pl','Project leader')))
    company = models.ForeignKey(Company, on_delete = models.CASCADE)