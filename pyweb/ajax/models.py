from django.db import models

# Create your models here.
class Keyword(models.Model):
    word=models.CharField(max_length=50, null=False)