from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    status_choices=[('draft','DRAFT'),('published','published')]
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=200,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=status_choices,default='draft')
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title
