from django.shortcuts import render
from .models import Test
from django.http.response import HttpResponse


# Create your views here.
def register(request):     # 나중에 url을 지정해줄건데, 해당 url로 접속 시 받게 될 매개변수가 request
    if request.method =="GET":
        return render(request, 'register.htm')
    elif request.method =="POST":
        username = request.POST['username'] # register 페이지에서 응답이 온다. 그게 GET이거나 POST이다.
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if password is not re_password:
            res_data['error'] = "비밀번호가 다릅니다!"
             
        else:
            res_data['error'] = ''
            fcuser = Test(  # 그러면 모델에서 Test 테이블을 가져와
                username=username,  # username과
                password=password   # password를 저장한다.
            )
            fcuser.save()   # 생성된 값은 저장한다.

        return render(request, 'register.htm', res_data)  # 다시 register 화면을 render한다(띄운다) (, , view에서 사용된 인자 전달)

        # 반환하고 싶은 파일 입력, 경로는 templates를 자동으로 바라보고 있으므로 생략
        # 만약 templates안에 하위 폴더가 존재한다면, folder/folder2/register.html 등으로 표기!
