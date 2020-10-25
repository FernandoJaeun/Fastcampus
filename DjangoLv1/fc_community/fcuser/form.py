from django import forms
from fcuser.models import Fcuser
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from django.shortcuts import redirect

# html 파일에서 form 태그안에 들어갈 내용


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': "아이디를 입력해주세요"
        },
        max_length=24,
        label="사용자 이름")
    password = forms.CharField(
        error_messages = {
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput,
        label="비밀번호", )
    user_id = '';

    def clean(self):  # forms.From 내장함수/ 유효성 검사 커스터마이징
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if (username and password):
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                self.user_id = fcuser.id # self는 LoginForm 자기자신