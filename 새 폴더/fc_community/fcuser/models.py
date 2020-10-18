from django.db import models

# Create your models here.

class Fcuser(models.Model):
    uesername = models.CharField(max_length=50, verbose_name = "사용자명")
    password = models.CharField(max_length=50, verbose_name = "비밀번호")
    registered_dtm = models.DateTimeField(auto_now_add = True, verbose_name = "비밀번호")

    class Meta:
        db_table = 'fastCampus_fcuser' # 테이블 명 지정