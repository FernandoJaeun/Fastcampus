from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.models.DateTimeField(auto_now_add=True, # 날짜 기입을 생략하면 자동으로 현재 날짜 입력
                                                  verbose_name='등록시간')

    class Meta: # DB에서 테이블 명을 지정하고 싶을 때.
        db_table  = 'fastcampus_fcuser'