# Section 10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 런타임 예외가 발생하기도 함
# # SyntaxError : 문법적 에러
# print('Test')

# if True
#     False

# x => y

# # 이런거

# # NameError : 선언되지 않은 변수
# a = 10
# b = 6
# print(c)

# # ZeroDivisionError : 0으로 나눌 때 에러 발생
# print(10/0)

# # IndexError : 요소를 가져올 때 해당 위치가 메모리상에 존재하지 않을 때
# a = [1,2,3] 
# print(a[4])


# # KeyError : 딕셔너리에서 키 값이 없을 떄
# dic ={'a':'1','b':'2','c':'3','d':'4'}
# print(dic['f'])

# print(dic.get('f')) # 얘는 에러가 아니러 NOne을 리턴


# # AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# # time 모듈에 month() 라는 속성이 없는데 그걸 호출하면 이 에러 발생
# import time
# print(time.time())


# # ValueError : 참조 값이 없을 때 발생
# x : [1,5,78]
# x.remove(10)

# # FileNotFoundError
# with open('./tes123t.txt' , 'r') as f:
#     content = f.read()

# TypeError : String과 Int를 더하는 경우 발생(예)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그후 런타임 예외 발생시 예외 처리 코딩 권장!!!( EAFP 코딩 스타일 )


# 예외 처리 기본
# try
# except : 예외 처리1
# except : 예외 처리2
# else : 예외가 발생하지 않았을 경우 실행
# finally : 항상 발생

# 예제 1

name = ['Kim','Lee','Park']

try:
    z = 'Kim2'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+3))
except ValueError:
    print("Not Found it")
else:
    print("OK! else!")


try:
    a = 123
    if a!= 1223:
        raise ValueError    #  강제로 에러 발생
except ValueError :
    print('문제발생')

