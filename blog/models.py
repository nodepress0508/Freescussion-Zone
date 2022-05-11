from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
# Create your models here.
class Post(models.Model):
    title  = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #new design
    # post_img = models.ImageField(upload_to='images/')
    #end new design
    def __str__(self):
        return self.title

    def get_absolute_url(self):#after create post, go to post detail page
        return reverse('post-detail',kwargs={'pk':self.pk})