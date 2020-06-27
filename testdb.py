# import sqlite3
# conn = sqlite3.connect('mydb.db')

# # Cursor 객체 생성
# c = conn.cursor()

# # 테이블 생성
# c.execute("CREATE TABLE student (num varchar(50), name varchar(50))")

# # execute 에 db 에 적용
# conn.commit()

# # 접속한 db 닫기
# conn.close()

################################################################################

# import sqlite3
# conn = sqlite3.connect('mydb.db')

# # Cursor 객체 생성
# c = conn.cursor()

# # 데이터 삽입
# c.execute("INSERT INTO student VALUES ('20201234', '파이썬')")
# # c.execute("INSERT INTO student VALUES ('20201235', 'VSCODE')")
    
# # execute 에 db 에 적용
# conn.commit()

# # 접속한 db 닫기
# conn.close()

#################################################################################


# import sqlite3
# conn = sqlite3.connect('mydb.db')

# # Cursor 객체 생성
# c = conn.cursor()

# # 데이터 불러 와서 출력
# for row in c.execute('SELECT * FROM student'):
#     print(row)

# # 접속한 db 닫기
# conn.close()


#################################################################################



import sqlite3
conn = sqlite3.connect('mydb.db')

# Cursor 객체 생성
c = conn.cursor()

# 학번을 검색해서 정보 출력

num = ('20201235',)
# num = '20201234'

c.execute('SELECT * FROM student WHERE num = ?', num)
# c.execute('SELECT * FROM student WHERE num = %s'% '20201235')    # SELECT * FROM student WHERE num = '20201234' 와 똑같다 보안이 취약해서 쓰지않는걸추천

print(c.fetchone())

# 접속한 db 닫기
conn.close()



#################################################################################



# CREATE TABLE "users" (
# 	"id"	varchar(50),
# 	"pw"	varchar(50),
# 	"name"	varchar(50),
#     PRIMARY KEY("id")
# );


