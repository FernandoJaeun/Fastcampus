# 코딩의 핵심 -> 조건 해결 중요
# 기본 반복문 : for while

v1 = 1
while v1 < 10:
    print("v1 is : " , v1)
    v1 += 1

print("\n\n")

for v2 in range(10):
    print("v2 is : ", v2)

for v3 in range(1000):
    print("v3 is : ", v3)

# 시퀀스(순서가 있는 자료형 반복)
# **문자열**, 리스트, 튜플, 사전, 집합(Set)
# 문자열은 시퀀스다!! 리스트같은!! 중요~

word = "LeejaeYun"
for v in word:
    print(v)

myInfo = {
    "name" : "Kim",
    "age" : 25,
    "city" : "Seoul"
}

for key, value in myInfo.items():
    print(key)

for key, value in myInfo.items():
    print(value)

for value in myInfo.items():
    print(value)


# break
numbers = [1,2,3,4,5,6,7]
for number in numbers :
    if number == 4:
        print(number)
        break

print("\n\n")
# continue
numbers = [1,2,3,4,5,6,7]
for number in numbers :
    if number == 4:
        continue
    print(number)

print("\n\n")

for number in numbers:
    if(number == 5):
        print("good")
        break
    else:
        print("bad")
else:   # for문의 else~!!! good~~~!!
    print("end of for")
