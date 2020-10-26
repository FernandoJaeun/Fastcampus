from django import forms
from .models import Board
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from django.shortcuts import redirect

# html 파일에서 form 태그안에 들어갈 내용


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': "제목을 입력해주세요"
        },
        max_length=128,
        label="제목")
    contents = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요'
        },
        widget=forms.TextInput, label="내용", )
