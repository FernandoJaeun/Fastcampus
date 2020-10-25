from django.shortcuts import render
from django.http import HttpResponse
from .models import Board



def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, "board_list.htm", {'boards': boards})
