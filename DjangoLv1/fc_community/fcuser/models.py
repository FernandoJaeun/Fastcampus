from django.db import models

# Create your models here.
class Test(models.Model):
    username = models.CharField(max_length=14)
    password = models.CharField(max_length=10, null=True)
    class Meta:
        db_table = "asd"
        verbose_name = "패스트 캠퍼스 사용자"   # 관리자 페이지에 표시될 모델 이름
        verbose_name_plural = "패캠"    # 모델 복수 이름(defalut는 복수로 표시됨)

    # 클래스가 변환됐을 때 호출되는 함수
    def __str__(self):  # string임. 내부클래스. 이 클래스에 입력된 값을 문자열(uesrname)로 반환
        return self.username, self.password