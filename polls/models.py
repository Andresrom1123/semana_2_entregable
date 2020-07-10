from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    classroom = models.ManyToManyField(Classroom)
    name = models.CharField(max_length=200)
