from django.contrib import admin
from .models import Fcuser  # 모델안 Fcuser 모델


# Register your models here.
class FcuesrAdmin(admin.ModelAdmin):
    list_display = ('username','useremail', 'password')    # fcuser App - 전체 내용 표시?

admin.site.register(Fcuser, FcuesrAdmin)