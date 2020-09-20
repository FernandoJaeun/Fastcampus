# Section02-2
# 파이선 기초 코딩
# 몸풀기 코딩 실습

# 파이썬 창조자의 철학 ㅋㅋ 재밌다
# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)  # 입력 인코딩의 기본은 UTF-8이고,
print(sys.stdout.encoding)  # 출력 인코딩의 기본도 UTF-8이다.

# 출력문
print('My name is Goodboy!')

# 변수 선언
Myname = 'Goodboy'

# 조건문
if Myname == "Goodboy":
    print('Ok')  # indent 들여쓰기

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i*j))

# 변수 선언(한글)
이름 = "좋은 사람"
print(이름)


# 함수 선언
def 인사():
    print("안녕하세요 반갑습니다")

인사()


# 클래스
class Cookie:
    pass


# 객체 생성
cookie = Cookie()
print(id(cookie))
print(dir(cookie))






