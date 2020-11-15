from django.shortcuts import redirect, render
from django.views.generic.edit import FormView

from .forms import RegisterForm, LoginForm
# Create your views here.


def home(request):
    return render(request, 'home.htm' , { 'email' : request.session.get('user') })


class RegisterView(FormView):
    template_name = 'register.htm'  # 연동할 template
    form_class = RegisterForm       # 가져올 Class-based-View
    success_url = '/fcuser/login'      # 이동할 url


class LoginView(FormView):
    template_name = 'login.htm'
    form_class = LoginForm
    success_url = '/'

    # session 저장
    def form_valid(self, form): # form이 정상작동 했을 때 실행되는 함수
        self.request.session['user'] = form.email
        return super().form_valid(form) 
    

def logout(request):
    if request.session.get('user'):
        print('user')
        del(request.session['user'])

    return redirect('../login')