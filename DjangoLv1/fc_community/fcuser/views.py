from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Test
from django.core.mail.backends import console
import logging

logger = logging.getLogger(__name__)
# Create your views here.


def register(request):     # 나중에 url을 지정해줄건데, 해당 url로 접속 시 받게 될 매개변수가 request
    if request.method == "GET":
        return render(request, 'register.htm')
    elif request.method == "POST":
        # register 페이지에서 응답이 온다. 그게 GET이거나 POST이다.
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)  # 화면으로 부터 받은 데이터
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not (username and useremail and password and re_password):
            res_data['error'] = "모든 값을 입력해주세요"
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다!"
        else:
            fcuser = Test(  # 그러면 모델에서 Test 테이블을 가져와
                username=username,  # username과
                useremail=useremail,
                password=make_password(password)   # password를 저장한다.
            )
            fcuser.save()   # 생성된 값은 저장한다.

        # 다시 register 화면을 render한다(띄운다) (, , view에서 사용된 인자 전달)
        return render(request, 'register.htm', res_data)

        # 반환하고 싶은 파일 입력, 경로는 templates를 자동으로 바라보고 있으므로 생략
        # 만약 templates안에 하위 폴더가 존재한다면, folder/folder2/register.html 등으로 표기!


def login(request):
    if request.method == "GET":
        return render(request, "login.htm")

    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (useremail and password):
            res_data['error'] = "모든 값을 입력하세요."
        else:
            # key - value (이메일이 정보를 get)
            fcuser = Test.objects.get(useremail=useremail)
            if check_password(password, fcuser.password):
                # 세션 - 쿠키 설정 로그인 정보 유지
                request.session['user'] = fcuser.id
                return redirect('/')  # 홈
            else:
                res_data['error'] = "패스워드가 일치하지 않습니다."
        return render(request, "login.htm", res_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Test.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('home')  # 세션을 날리는 방법은?
