from django.db import models
from app.models import *

# Create your models here.
class school(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
