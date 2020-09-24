# 타이핑 게임 제작

import random
import time

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

    if question == answer:
        correct_count += 1
        print('pass')
    else:
        print('fail')

    n += 1

end = time.time()  # 게임 종료 시간
running_time = end - start

if correct_count >= 3:
    print('합격')
else:
    print('불합격')

print('')
print('"게임 시간 : %.2f | 정답 개수 : %s' % (running_time, correct_count))

