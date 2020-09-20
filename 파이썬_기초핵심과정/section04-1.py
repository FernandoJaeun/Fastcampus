# 데이터 타입
v_str1 = "NcieMan" # 문자열 하나가 변수에 할당됨
v_bool1 = True # 참,거짓 중 하나가 변수에 할당됨
v_str2 = "Goodboy" # 문자열 하나가 변수에 할당됨
v_floot = 10.3 # 실수 하나가 변수에 할당됨
v_int = 10 # 정수하나가 변ㅂ수에 할당됨
v_dict = {
    "name" : "Kim",
    "age" : 25
}   # 사전형 데이터 타입

v_list = [3,5,7]
v_tuple = 3, 5, 7
v_set = {3,5,7}
print(v_list)
print(type(v_dict))

i1 = 10
i2 = 5
print(i1 * i1)
print(i1 ** i1)

print(i2 * i2)
print(i2 ** i2)
big_int1 = 111111111111111111111111111111111111111111111111111111111
big_int2 = 1231231231908310984284128940128975203985710589712059871205897
print(big_int1)
print(big_int2)
print(type(big_int1))
print(type(big_int2))



f1 = 1.123
f2 = 3.515
f3 =.123
f4 = 10.

print(f1)
print(f2)
print(f3)
print(f4)
print(type(f3))
print(type(f4))

a= 5.
b =4 

print(type(a), type(b))

print(int(a))
print(a)
print(complex(3))
print(int(True))
print(int('3'))
print(complex(False))



# 수치 연산
y = 100
y += 100
print(y)

y *= 100
print(y)

y = -y
print(y)
print(abs(y))

print(complex(10,5))
print(pow(10, 3))
print(pow(10, 5))

print(divmod(10,3))
a,b = divmod(55,5)
print(a)
print(b)

import math
print(math.trunc(10.123))
print(type(math.trunc(1000.1)))
print(type(math.trunc(33132.)))


print(math.ceil(5.1))   # x 이상의 수 중에서 가장 작은 정수
print(math.ceil(8.999))

print(math.floor(3.874)) # x 이하의 수 중에서 가장 큰 정수
print(math.floor(-25.5))
print(math.pi)
print(bin(50)) #0b로 시작
