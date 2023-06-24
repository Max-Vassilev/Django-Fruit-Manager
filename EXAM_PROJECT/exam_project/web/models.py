from django.db import models
from django.core.validators import MinLengthValidator
from exam_project.web.validators import alpha_only, alpha_first


class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=[MinLengthValidator(2), alpha_first])
    last_name = models.CharField(max_length=35, validators=[MinLengthValidator(1), alpha_first])
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    image_url = models.URLField(null=True, blank=True)
    age = models.IntegerField(default=18)


class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2), alpha_only])
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(null=True, blank=True)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

