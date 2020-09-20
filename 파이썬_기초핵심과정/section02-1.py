# Section02-1
# 파이썬 기초 코딩
# 프린트 구문의 이해

# 기본출력 자료형 : 숫자, 문자 등등..

print('Hello World!')
print("Hello World!")

# '' 와 "" 차이는 뭘까? : 말 안 해주네...

print("""Hello Pyhon!""")
print('''Hello Pyhon!''')

# ''' ''' 는 뭐고 """ """ 는 뭘까?

print()

# Separator 옵션 사용

print('T','E','S','T')
print('T','E','S','T', sep = '')

# sep는 출력되는 문자들이 여러 개 일때, 문자들 사이에 들어갈 문자를 입력하는 옵션이구나


# End 옵션 사용

print('Welcom To', end = ' ')
print('the black Parade', end = '')

# end는 출력되는 문자의 끝을 지정하는 옵션이구나. 즉 print는 요소를 출력 후 자동으로 줄 바꿈(\n)을 붙인다.
# 하지만 end = ''을 선언하게 되면 줄 바꿈이 사라지는 효과를 줄 수 있다.


# Format 사용 [], {}, () 대 중 소 괄호
print("")
a = "asd"
b = "das"

print(f'{a} and {b}')
print('{} and {}' .format("asd", "asd"))
print('{1} and {0} and {1}'.format("a","b","c"))
print('{a} and {b}'.format(a=13, b= 3123))

print('%5d , %4.2f' % (776123, 654321.12345)) # 표시할 숫자의 자릿수 지정. 이거 나중에 값 표현할 떄 쓰면 좋겠다.

print("{0:5d}, {1:4.2f}".format(1234567, 123456.1234))

a= 12345678
b= 12345.123

print(f"{a:5d} {b}")
print('\'')
print('\'you\'')
print('me\tmew\n')
print("test")