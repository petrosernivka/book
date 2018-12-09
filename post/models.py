# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Meta():
        db_table = 'post'

    post_title = models.CharField(verbose_name="", max_length = 200)
    post_text = models.TextField(verbose_name="")
    post_date = models.DateTimeField()
    post_likes = models.IntegerField(default=0)
    post_unlikes = models.IntegerField(default=0)
    post_author = models.ForeignKey(User, on_delete=models.PROTECT)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_date = models.DateTimeField()
    comments_text = models.TextField(verbose_name="")
    comments_post = models.ForeignKey('Post', on_delete=models.PROTECT)
    comments_author = models.ForeignKey(User, on_delete=models.PROTECT)
