from django.db import models
from django.contrib.auth.models import User


class ItemAbstract(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PhotoItem(ItemAbstract):
    image = models.ImageField()


class TweetItem(ItemAbstract):
    text = models.CharField(max_length=150)

    def __unicode__(self):
        return self.text
