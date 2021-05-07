from django.db import models


class Addname(models.Model):
  name = models.CharField(max_length=100)

