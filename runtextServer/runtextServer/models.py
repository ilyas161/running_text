from django.db import models


class Texts(models.Model):
    running_text = models.CharField(max_length=200)