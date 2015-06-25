from django.shortcuts import render, render_to_response
from django.db.models import Q

from stream.models import Stream

def home(request):
    query_photos = Q(photo__deleted=False) & Q(tweet=None)
    query_tweets = Q(tweet__deleted=False) & Q(photo=None)
    results = Stream.objects.filter(query_photos | query_tweets)
    print results
    return render_to_response('home.html', {'results': results})
