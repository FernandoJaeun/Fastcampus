ㄴㅇimport sqlite3

# DB 생성(파일)
conn = sqlite3.connect('./resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceMan' , 2))
conn.commit()

# 데이터 수정2
c.execute("UPDATE users SET username =:name WHERE id =:id", {'name': 'GoodMan', 'id': 3})
conn.commit()

# 데이터 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'"% ('Baby',4) )
conn.commit()

# 중간 데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)

# 데이터 삭제 1
c.execute("DELETE FROM users WHERE id = ?" , (2,))
conn.commit()

c.execute("DELETE FROM users WHERE id = :id", {'id': 5})
conn.commit()

c.execute("DELETE FROM users WHERE id ='%s' " % 4)
conn.commit()

# 중간 데이터 확인2
for user in c.execute("SELECT * FROM users"):
    print(user)

print('delete all data from database.db', conn.execute("DELETE FROM users").rowcount,"rows")
conn.commit()
conn.close()

