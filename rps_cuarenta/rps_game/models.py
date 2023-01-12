from django.db import models

# Create your models here.
class UserSelection(models.Model):
    selection = models.CharField(max_length=100)
    computerSelection = models.CharField(max_length=20)

class Status(models.Model):
    stat = models.CharField(max_length=5)
    score = models.IntegerField()
    outof = models.IntegerField()