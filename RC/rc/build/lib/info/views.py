from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
    # username = request.user.id
    return HttpResponse('list')

def add(request, n_id=None):
    if n_id == None:
        return HttpResponse('add')
    else:
        return HttpResponse('modify')

def read(request, n_id):
    return HttpResponse('read')

# def modify(request, id):
#     return HttpResponse('modify')

def delete(request, n_id):
    return HttpResponse('delete')