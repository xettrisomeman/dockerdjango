from django.shortcuts import render

import redis 


cache = redis.Redis(host='redis')

tries = cache.set('tries' , 5)
zero=cache.set('zero',0)

def index(request):
    decreaseTries = cache.decr('tries')
    print(f"You will be redirected after {decreaseTries} refreshes")
    if decreaseTries==zero:
        return render(request , 'About.html')
    return render(request ,'home.html')


