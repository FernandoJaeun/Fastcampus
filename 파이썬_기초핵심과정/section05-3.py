q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if "가을" in q1:
    print(q1["가을"])


q2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
if "사과" in q2.values():
    print("사과 있다")

a = 5
b = 6
c = 6
best = 0

if a > b and a > c:
    best = a
elif b > a and b > c:
    best = b
else :
    best = c
print(best)
    

s = '891022-5473837'
idx = s.index("-")+1
if s[idx] == "1" or idx =="3":
    print("남자")
elif s[idx] == "2" or idx =="4":
    print("girl")
else:
    print("누구?")

q3 = ["갑", "을", "병", "정"]
for v in q3:
    if v is not "정":
        print(v)

for v in range(1,100,2):
    print(v, end=" ")

q4 = ["nice", "study", "python", "anaconda", "!"]
for i in range(len(q4)):
    if len(q4[i]) >= 5:
        print(q4[i])
print([s for s in q4 if len(s)>=5 ])


q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print([s for s in q5 if s.islower()])


q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print([s.upper() if s.islower() else s.lower() for s in q6])
