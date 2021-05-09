#from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404, render
#from django.urls import reverse
#from django.views import generic

#from .models import Choice, Question
from django.http import HttpResponse

def cookieplay(request):
    if 'view_count' in request.COOKIES:
        vc = int(request.COOKIES['view_count'])
    else: vc=0
    vc+= 1

    resp=HttpResponse('Secret: 0029f088. view count=' + str(vc))
    resptext = 'Secret: 0029f088.'
    resp.set_cookie('dj4e_cookie', '0029f088', max_age=1000)
    resp.set_cookie('view_count', str(vc))
    return resp

