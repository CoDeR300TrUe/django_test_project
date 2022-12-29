from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        name = ('Комментарий от ' + str(self.author) + '. Пост: ' + str(self.post) + '. Контент: ' + str(self.content))
        return name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})


class Rating(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Post, on_delete=models.CASCADE)
    argument = models.CharField(max_length=10, default='none')

    def __str__(self):
        name = str(self.profile) + ' ' + str(self.publication)
        return name