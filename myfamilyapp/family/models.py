from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class CodingSession(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    duration_minutes = models.IntegerField()
    date = models.DateField()

class PlaytimeSession(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    duration_minutes = models.IntegerField()
    date = models.DateField()
