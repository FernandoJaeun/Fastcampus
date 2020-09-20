# Section04-3
# 파이썬 데이터 타입(자료형)

name ='Lee'
name2 = 'Park'
name3 = 'Choi'
# ... 같은 이름 항목인데 변수를 자꾸 만드는 건 에바!
# 그래서 아래와 같이 묶어준다
name = ['Lee', 'Park', 'Choi']

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'String', 'is Ok']
e = [10, 100, ['double', 'List', 'Tambien', 'is OK']]
# 슬라이싱
print(d[3])
print(d[1:3])
print(d[-1])
print(d[-1::-1])
print(e[2][0:])
print(e[2][::-1])

# 연산
print(c+d)
print(c + e[2][:3])
print(c * 3)

# 리스트 수정, 삭제
print(c)
c[1:1] = [10,100,100]
print(c)
del c[0:2]
print(c)


y = [1,2,3,4,5]
y.insert(len(y),55)
y.insert(len(y),56)
y.insert(len(y),57)
print(y)

ex = [123,456]
y.extend(ex)
print(y)


# 튜플은 리스트와 똑같지만, 파이널형식 이다!! 순서변경, 중복 값은 허용하지만, 추가 삭제가 불가능하다!!
a = ()
b = (1,)
c = (1,2,3,4)
d = c + ('a','b','c')

print(a)
print(d)