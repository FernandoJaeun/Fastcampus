# SQLite DB Python과 연동

# 테이블 생성 및 삽입

import sqlite3 # 기본 패키지에 sqlite3가 포함되어있다
import datetime

# sqlite 3 안에 sqlite가 있다?
print(sqlite3.version)
print(sqlite3.sqlite_version)


now = datetime.datetime.now()
print(now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDateTime)


# DB 생성 및 Auto Commit(Roll Back) 다시 되돌리는거, 복군데 말을 바꿔쓰나보다 모든 프로그램 파일은 롤백 기능이 기본적으로 있는 듯
conn = sqlite3.connect('C:/Users/leeja/WorkSpace/Python/FastCampus/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor() # conn이라는 DB로 눈을 돌림 (나는 사우론이다)

# 테이블 생성(데이터 베이스)
# c.execute("CREATE TABLE IF NOT EXISTS users(\
#     id INTEGER PRIMARY KEY, \
#     username text, \
#     email text, \
#     phone text, \
#     website text,\
#     regdate text \
#     )")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'Kim', 'kim@naver.com', '010-0000-0000','kim.com',?)",(nowDateTime,))
# c.execute("INSERT INTO users (id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Lee', 'leejaeyun95@naver.com', '010-8589-2763', 'fercho@naver.com', nowDateTime))


# 많은 데이터를 한 번에 INSERT 하는 방법!!!! Many 삽입(튜플, 리스트)
# userList = (
#     (3, 'Lee', 'Lee@naver.com' ,'01012345566' ,'Lee.com' , nowDateTime ),
#     (4, 'Cho', 'Cho@naver.com' ,'01012345566' ,'Cho.com' , nowDateTime ),
#     (5, 'Yoo', 'Yoo@google.com' ,'01012345566' ,'Yoo.com' , nowDateTime ),
# )

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

# conn.execute("DELETE FROM users")
# print('delete db Table : ', conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 오토 커밋
# conn.commit() db에 삽입이 호출된 이후 자동으로 이 메소드가 호출됨

# conn.rollback() 어따 쓰노
# conn.close() db 종료
