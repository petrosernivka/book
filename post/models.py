from django.db import models

class Post(models.Model):
    class Meta():
        db_table = 'post'

    post_title = models.CharField(max_length = 200)
    post_text = models.TextField()
    post_date = models.DateTimeField()
    post_likes = models.IntegerField(default=0)
    post_unlikes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_post = models.ForeignKey('Post', on_delete=models.PROTECT)
