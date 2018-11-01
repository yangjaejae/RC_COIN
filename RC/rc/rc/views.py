from django.shortcuts import render

# Create your views here.

<<<<<<< HEAD
def home(request):
    return render(request, './home.html', dict({}))
=======
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
>>>>>>> 3980f1f67d7d6b1655dc042a651dfed059c1fef1
