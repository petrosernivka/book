from django.contrib import admin
from post.models import Post, Comments


# Register your models here.
class PostInline(admin.StackedInline):
    model = Comments
    extra = 3


class PostAdmin(admin.ModelAdmin):
    exclude = ['post_likes', 'post_unlikes']
    inlines = [PostInline]
    list_filter = ['post_date']


admin.site.register(Post, PostAdmin)
