from django.contrib import admin
from .models import Test  # 모델안 Test 모델


# Register your models here.
class FcuesrAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone')    # fcuser App - 전체 내용 표시?

admin.site.register(Test, FcuesrAdmin)