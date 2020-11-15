from django import forms

from django.db.utils import IntegrityError

from django.contrib.auth.hashers import check_password, make_password

from .models import Fcuser

# Class-based-Views


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        label="이메일"
    )

    password = forms.CharField(
        error_messages={
            'required':  '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    re_password = forms.CharField(
        error_messages={
            'required':  '비밀번호 확인을 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()  # 입력 형식을 충족한 데이터
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        # 이메일 중복 검사
        try:
            Fcuser.objects.get(email=email)
            self.add_error('email', '이미 사용중인 이메일입니다.')
        # 비밀번호 일치 검사
        except:
            if password and re_password:
                if password == re_password:
                    fcuser = Fcuser(
                        email=email,
                        password=make_password(password)    # 암호화
                    )
                    fcuser.save()
                else:
                    self.add_error('re_password', '패스워드가 서로 일치하지 않습니다')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요'
        },
        label="이메일"
    )

    password = forms.CharField(
        error_messages={
            'required':  '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password:
            print(email)
            try:
                fcuser = Fcuser.objects.get(email=email)
            except Fcuser.DoseNotExist:
                self.add_error('email', '존재하지 않는 이메일입니다')

            # DB 값 참조
            if check_password(password, fcuser.password):   # 암호화 유무에 따라 같은 암호도 다르게 인식하여 Reject
                self.email = fcuser.email
            else:
                self.add_error('password', '비밀번호를 틀렸습니다.')