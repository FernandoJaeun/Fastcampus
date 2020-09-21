# 파일 읽기, 쓰기
# 읽기 모드 : r
# 쓰기 모드 : w
# 추가모드(파일 생성 및 내용 추가) : a
# .. : 상대경로
# . : 절대 경로

f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
f.close()
# 파일 사용이 끝난 후 닫지 않으면 계속 열려 있게 되고, 프로그램이 돌다가 언젠간 오류가 나기떄문에 닫아준다
print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/review.txt', 'r') as f : # with문은 자동으로 close 해준다
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 한번 read하게되면 커서가 content의 젤 끝으로 이동한 채로 끝난다. 
                        # 두번째 read는 커서의 위치가 젤 끝이라 읽으게 없어서 공백 리턴
    print(">", content) 

    
print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/review.txt', 'r') as f:   
    line = f.readline()
    while line:
        print(line, end= '###')
        line = f.readline() # readline()은 한줄씩 읽는 메소드이고, 한줄을 읽으면 커서는 그 줄 마지막으로 이동하니
            # 다음 readline()이 오면 다음 줄을 읽는다. 그러다 젤 마지막 라인을 읽으면 끝. while문은 읽을게 없으니 False
            
print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/review.txt', 'r') as f:   
    contents = f.readlines()    # readline과 readlines의 큰 차이!
    print(contents)
    for c in contents:
        print(c, end = "******")

print()
    
    
print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f :
        score.append(int(line))
    print(score)
print("평균 : {:3.3}".format(sum(score)/len(score)))

print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/text1.txt', 'w') as f:
    f.write("NiceMan!!")

with open('./resource/text1.txt', 'a') as f:
    f.write("NiceMan!!")

from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

print('---------------------------------------------')
print('---------------------------------------------')

with open('./resource/text2.txt', 'w') as fs:
    list = ['Kim\n', 'Park\n', 'Sep\n']
    fs.writelines(list) # 리스트를 쓰는 메소드 writelines

    with open('./resource/text3.txt', 'w') as f:
        print('Test!!', file = f)
        print('Test!!!!!', file = fs)
