from django.shortcuts import render
from django.template import loader
from django.urls.http import HttpResponse

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
