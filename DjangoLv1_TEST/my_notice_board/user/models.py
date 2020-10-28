from django.db import models

# Create your models here.

class USER(models.Model):
    username  = models.CharField(max_length = 12 , verbose_name="사용자 이름")
    email = models.EmailField(max_length = 64, verobose_name = "사용자 이메일", primary_key = True, Unique = True)
    password = models.CharField(max_length=16, verbose_name ="사용자 비밀번호")
    registerd_dttm = models.DateTimeField(auto_now=True, auto_now_add=True, verbose_name="생성일")

    def __str__(self):
        return self.username, self.registerd_dttm
    class Meta:
        verbose_name = "사용자 정보"
        ordering = ['-registerd_dttm', ]