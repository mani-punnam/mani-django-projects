from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE,related_name='articles')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article2(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication,related_name='articles')

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
    def get_publications(self):
        return "\n".join([p.title for p in self.publications.all()])

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        related_name='restaurants',
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,related_name='waiters')
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
