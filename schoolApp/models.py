from django.db import models
from django.utils import timezone

# Create your models here.


class Teacher(models.Model):
    name=models.CharField(max_length=80)
    subject=models.CharField(max_length=80)
    hours=models.PositiveIntegerField()
    workDate=models.DateField()
    entryDate=models.DateTimeField(default=timezone.now())
    school=models.CharField(max_length=80)

    def __str__(self):
        return self.name


