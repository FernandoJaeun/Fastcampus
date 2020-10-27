from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Home")

def login(request):
    return render(request, 'signin.htm' )

def register(request):
    return HttpResponse("register")
