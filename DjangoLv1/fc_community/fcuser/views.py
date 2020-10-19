from django.shortcuts import render

# Create your views here.
def register(request):     # 나중에 url을 지정해줄건데, 해당 url로 접속 시 받게 될 매개변수가 request
    if request.method =="GET":
        return render(request, 'register.htm')
    elif request.method =="POST":
        return render(request, 'register.htm')

    return render(request, 'register.htm')  # 반환하고 싶은 파일 입력, 경로는 templates를 자동으로 바라보고 있으므로 생략
                                            # 만약 templates안에 하위 폴더가 존재한다면, folder/folder2/register.html 등으로 표기!
