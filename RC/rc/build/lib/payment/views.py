from django.shortcuts import render

# Create your views here.

def withdraw(request):
    print(1234, "##########################")
    return render(request, "payment/withdraw.html", ({}))

def history(request):
    return render(request, "payment/history.html", ({}))