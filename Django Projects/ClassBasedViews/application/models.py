from django.db import models
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    no_of_pages=models.IntegerField()
    price=models.IntegerField()
    def get_absolute_url(self):
        return reverse('home')
        #If you want to pass the arguments, you can write like this reverse('deatil',kwargs={'pk':self.pk})
