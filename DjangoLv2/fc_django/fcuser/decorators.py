from django.shortcuts import redirect
from .models import Fcuser

def login_required(function):
    def warp(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/fcuser/login')
        return function(request, *args, **kwargs)

    return warp
            

def admin_required(function):
    def warp(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/fcuser/login')

        user = Fcuser.objects.get(email = user)
        if user.level != 'admin':
            return redirect('/')
        
        return function(request, *args, **kwargs)

    return warp