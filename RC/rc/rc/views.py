from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def intro(request):
    template = loader.get_template('intro.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))


def map(request):
    template = loader.get_template('map.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
