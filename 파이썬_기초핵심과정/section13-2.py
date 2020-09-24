# 타이핑 게임 제작

import random
import time

import winsound # 소리재생을 도와주는 패키지
import sqlite3
import datetime

# DB 생성 & 오토커밋
conn = sqlite3.connect('./resource/recored.db', isolation_level=None)

# Cursor 획득
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS recordes( id INTEGER PRIMARY KEY AUTOINCREMENT, correct_count INTEGER, record text, regdate text)")


words = []  # 영어 단어 리스트 (1000개 로드)
n = 1  # 게임 시도 횟수
correct_count = 0  # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for word in f:
        words.append(word.strip())

# print(words) # 단어 확인

input("Ready? Prees Enter Key!")  # Enter Game Strat!

if __name__ == "__main__":
    pass

start = time.time()  # 게임 진행 시간

while n <= 5:
    random.shuffle(words)  # 섞는다
    question = random.choice(words)  # 뽑는다
    print('')
    print('*Question #{}'.format(n))
    print(question)  # 문제 출력

    answer = input()

    if str(question).strip() == str(answer).strip():
        correct_count += 1
        print('pass')
        # 정답 소리
        winsound.PlaySound('./resource/sound/good.wav', winsound.SND_FILENAME)
    else:
        print('fail')
        # 오답 소리
        winsound.PlaySound('./resource/sound/bad.wav', winsound.SND_FILENAME)
    n += 1

end = time.time()  # 게임 종료 시간
running_time = end - start

if correct_count >= 3:
    print('합격')
else:
    print('불합격')

print('')
c.execute("INSERT INTO recordes('correct_count', 'record', 'regdate') VALUES ( ?, ?, ? )" ,  (correct_count, running_time, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))) 
print('"게임 시간 : %.2f | 정답 개수 : %s' % (running_time, correct_count))

