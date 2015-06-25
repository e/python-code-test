from django.contrib import admin

from models import PhotoItem, TweetItem


class TweetItemAdmin(admin.ModelAdmin):
    list_display = ('id', '__unicode__', 'deleted',)
    list_filter = ('deleted',)

admin.site.register(TweetItem, TweetItemAdmin)


class PhotoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'deleted',)
    list_filter = ('deleted',)

admin.site.register(PhotoItem, PhotoItemAdmin)
