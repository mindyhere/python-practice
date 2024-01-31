from django.db import models

# Create your models here.
class Book(models.Model):
    idx=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50, blank=True,null=True)
    author=models.CharField(max_length=20, blank=True, null=True)
    price=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
