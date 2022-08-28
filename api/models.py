from django.db import models


class Players(models.Model):
    name = models.TextField()
    date_of_birth = models.DateField()
    place_of_birth = models.TextField()
    age = models.IntegerField()
    position = models.TextField()
    number = models.IntegerField()


class Coaches(models.Model):
    name = models.TextField()
    date_of_birth = models.DateField()
    place_of_birth = models.TextField()
    age = models.IntegerField()
    job_title = models.TextField()