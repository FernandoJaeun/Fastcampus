# Section04-4
# 파이썬 데이터타입(자료형)
# 딕셔너리, 집합 자료형

# Dictionary : 순서X 중복X 수정O 삭제O

# Key, Value : Json -> MongoDB

# 선언
a = {'name': 'Kim',
    'Phone' : '010'}

b= {0: 'asd',
    1: ' asdasd'}# 숫자로 지정하는 건 의미가 없음
c= {'arr' : [1,2,3,4,5]}

print(a['name'])
print(a.get('name'))
print(c.get('arr')[1:3])

a['Phone'] = 'Seout','asdas'
print(a.get('Phone'))
print(a.values())
print(a.keys())

temp = list(a.keys())
print(temp)

temp = list(a.values())
print(temp)

# 집합(Set) 순서X 중복X
a = set()
b = set([1,2,3,4])
c = set([1,3,4,5,6,6,7])
print(b)
print(c)

t = tuple(b)
print(t)
l = list(c)
print(l)

print(b.intersection(c))
print(b & c)

print(b.union(c))
print(b|c)

print(b.difference(c))
print(c.difference(b))

b.add(123)
print(b)
b.remove(123)
print(b)