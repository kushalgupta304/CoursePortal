from django.db import models
from authentication.models import User
# Create your models here.




class Course(models.Model):
    c_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=400)
    educator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active= models.BooleanField(default=True)

class Enroll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

