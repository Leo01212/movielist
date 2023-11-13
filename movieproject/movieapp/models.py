from django.db import models

# Create your models here.
class movie_details(models.Model):
    name=models.CharField(max_length=50)
    des=models.TextField(max_length=250)
    im=models.ImageField(upload_to='pic')
    year=models.IntegerField()

    def __str__(self):
        return self.name


