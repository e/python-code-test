from django.db import models
from django.contrib.auth.models import User

from items.models import PhotoItem, TweetItem

class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    photo = models.ForeignKey(PhotoItem, blank=True, null=True)
    tweet = models.ForeignKey(TweetItem, blank=True, null=True)

    def __unicode__(self):
        if self.tweet:
            return self.tweet.text
        elif self.photo:
            return 'Image ' + str(self.photo.id)
        else:
            return 'Stream ' + str(self.id)
