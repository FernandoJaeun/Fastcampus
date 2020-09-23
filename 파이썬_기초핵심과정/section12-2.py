# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect("./resource/database.db")
# 커서 바인딩(불러온 DB로 시선집중! 사우론)
c = conn.cursor()

# 데이터 조회(전체) 
c.execute("SELECT * FROM users")

# # 커서 위치가 변경
# # 1개 로우 선택
# print('One -> ', c.fetchone())

# # 지정 로우 선택
# print('Three -> ', c.fetchmany(size = 3))

# # 전체 로우 선택
# print('All -> ', c.fetchall())

# print('All -> ', c.fetchall())

print('')

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print(row)

# 순회2
# for row in c.fetchall():
#     print(row)

# 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print(row)

# 위에서 테이블 조회가 이뤄진 후에 불러오는게 가능하다 순서가 다 있구나

print('')

# WHERE Retrievel1
# param1 = (3,)
# c.execute('SELECT * FROM users WHERE id = ?', param1)
# print('param1 : ', c.fetchall())
# print('param1 : ', c.fetchone())

# WHERE Retrievel2
# param2 = 4
# c.execute('SELECT * FROM users WHERE id ="%s"'% param2)
# print('param2 : ', c.fetchone())
# print('param2 : ', c.fetchall())


# WHERE Retrievel3
# c.execute('SELECT * FROM users WHERE id =:Id',{"Id":5} )
# print('param3 : ', c.fetchone())
# print('param3 : ', c.fetchall())


# WHERE Retrievel4
# param4 = (4,5)
# c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
# print('param4 : ', c.fetchall())


# Dump 출력
# with conn:
#     with open("./resource/test.sql", 'w') as f:
#         for line in conn.iterdump():
#             f.write(line +"\n")