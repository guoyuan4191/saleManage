from django.db import models

# Create your models here.
class SaleInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    email = models.EmailField()
    company = models.CharField(max_length=64)
    def __str__(self):
        return self.name

