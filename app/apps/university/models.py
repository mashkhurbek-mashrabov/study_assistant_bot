from django.db import models

from common.models import BaseModel


class Group(models.Model):
    name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(BaseModel):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    telegram_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name
