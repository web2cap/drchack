#from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
#from django.urls import reverse
#from django.views import generic

#from .models import Choice, Question
from django.http import HttpResponse

def myview(request):
    resp=HttpResponse('Secret: 0029f088')
    resp.set_cookie('dj4e_cookie', '0029f088', max_age=1000)
    #return resp
    menu  = {
        'pools' : 'A Polls Application',
        'hello' : 'Test the session',
        'autos' : 'Autos Application',
        'cats'  : 'Cats CRUD',
    }
    return render(request, 'home/main.html', context = {'menu' : menu})
