from django.db import models

from common.models import BaseModel
from university.models import Group


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quote(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes', blank=True, null=True)
    text = models.TextField()
    groups = models.ManyToManyField(Group, related_name='quotes')
    was_send = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text[0:100]
