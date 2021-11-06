from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    blog_title = models.CharField(verbose_name="Title", max_length=300) 
    blog_author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    blog_date = models.DateField(verbose_name="Date and Time")
    blog_read_time = models.IntegerField(verbose_name="Read Time")
    blog_tag = models.CharField(verbose_name="Tagline", default="Python", max_length=200)
    blog_content = models.TextField("Description")

    def __str__(self):
        return self.blog_title

    

    def get_absolute_url(self):
       # return reverse("article-details", args=(str(self.id)))
       return reverse("post-list")
    

