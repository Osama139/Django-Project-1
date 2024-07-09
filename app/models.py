from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False, unique=True)

    def __str__(self):
        return self.name


class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    status = models.CharField(max_length=50)
