from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=2500)
    answer = models.CharField(max_length=2500)
    date = models.DateTimeField(auto_now_add=True)


class LinkClick(models.Model):
    link_clicked = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True) 


