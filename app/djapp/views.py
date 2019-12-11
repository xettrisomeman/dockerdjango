from django.shortcuts import render

import redis 


cache = redis.Redis(host='redis')

tries = cache.set('tries' , 10)
five=cache.set('zero',0)

def index(request):
    decreaseTries = cache.decr('tries')
    data= {
        'redirect':f'{decreaseTries}'
    }
    if decreaseTries==five:
        return render(request , 'About.html')
    return render(request ,'home.html' , data)

