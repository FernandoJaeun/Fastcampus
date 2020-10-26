from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from .form import BoardForm


def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, "board_list.htm", {'boards': boards})


def board_write(requset):
    form = BoardForm()
    return render(requset, 'board_write.htm', {'form' : form})