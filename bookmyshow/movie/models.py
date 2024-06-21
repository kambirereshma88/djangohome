from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.movie_name + "added into table"