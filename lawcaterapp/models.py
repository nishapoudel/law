from django.db import models
from django.contrib.auth import get_user_model

from tinymce.models import HTMLField
from datetime import date


class Category(models.Model):
    cat_id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=1000)


    def __str__(self):
        return self.title


class Post(models.Model):
    post_id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    content = HTMLField()
    author = models.CharField(max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    publish=models.BooleanField()
    read=models.IntegerField(default=0)

    class Meta:
        ordering=['-post_id']

    def __str__(self):
        return self.title

    def convert_str_date(value):
        return timestamp.strptime(value, '%Y-%m-%d').date()



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)