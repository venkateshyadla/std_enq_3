from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length = 50)
    father_name = models.CharField(max_length = 50)
    email = models.EmailField()
    dob = models.DateField()
    enquiry_date = models.DateField()
    course = models.CharField(max_length = 60)
    branch = models.CharField(max_length = 60)
    std_id = models.AutoField(primary_key = True)