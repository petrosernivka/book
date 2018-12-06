from django.db import models

class Post(models.Model):
    class Meta():
        db_table = 'post'
    post_title = models.CharField(max_length = 200)
    post_text = models.TextField()
    post_date = models.DateTimeField()
    post_likes = models.IntegerField()
    post_unlikes = models.IntegerField()
