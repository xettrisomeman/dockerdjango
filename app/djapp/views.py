from django.shortcuts import render

import redis 


cache = redis.Redis(host='redis')

tries = cache.set('tries' , 5)

def index(request):
    return render(request ,'home.html')

