from django.conf import settings
from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.DO_NOTHING, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(default=True)
    body = models.TextField(max)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)