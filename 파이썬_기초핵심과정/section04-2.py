# Section04-2
# 문자열, 문자열 연산, 슬라이싱 !!!

str1 = 'I am a Boy'
str2 = 'Nice day'
str3 = '  '
str4 = str()
print(len(str1))    
print(len(str2))    
print(len(str3))    # 공백도 길이를 먹는다
print(len(str4))


# Escape
escape_str1 = "Do you have a girl friend? \"big mama\""
print(escape_str1)

escape_str2 = "i want Mac\t Book\t Pro!!!"
print(escape_str2)

# Raw String
raw_str1 = r'C:\Programs\Test\Bin'  # 이스케이프 선언 기호를 무시하고 그대로 출력하게!!
print(raw_str1)

# Multi Line 역슬래시 역할은 다음 라인으로 이어지게 해줌
multi = \
""" 
멀티라인
라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = '&'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "abcderf"
print(str_o1 * 10) 
print(str_o2 + str_o2 , sep = "  ")
print(str_o3 * 3 , sep = " ")
print( 'a' in str_o4)
print('x' not in str_o4)

# 문자열 형 변환
print(str(77))
print(type(str(77)))

print(str(77) + '3')

# 문자열 함수
a = "NiceMan"
b = 'oragne'

print(a.islower())
print(b.islower())

print(a.capitalize())
print(b.replace('o', 'blue'))

print(list(reversed(a)))
print((sorted(a)))

print(a[0:3])
print(a[:len(a)])
print(a[::2])
print(a[1:-1])
print(a[::-1])