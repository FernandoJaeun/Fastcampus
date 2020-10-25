from django.contrib import admin
from .models import Board  


# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)    # fcuser App - 전체 내용 표시?

admin.site.register(Board, BoardAdmin)# Register your models here.
