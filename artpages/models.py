# import the standard Django Model
# from built-in library
from django.db import models


# declare a new model with a name "GeeksModel"
class GeeksModel1(models.Model):
    # fields of the model
    title1 = models.CharField(max_length=200)
    description1 = models.TextField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title1


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()


class ContacIfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.first_name
