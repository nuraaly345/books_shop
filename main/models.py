from enum import auto
from typing import Text
from django.db import models

class ToDo(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    genre=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    year=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
