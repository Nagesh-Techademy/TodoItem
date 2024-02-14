from django.shortcuts import HttpResponse, render

# Create your views here. for demo
def home(request):
    return HttpResponse("Hello World!")
   # return render(request, "home.html")

