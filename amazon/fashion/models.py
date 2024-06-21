from django.db import models

# Create your models here.
class styles(models.Model):
    fashion_name = models.CharField(max_length=50)
    delivery_date = models.DateField()

    def __str__(self):
        return self.fashion_name + "added into table"

