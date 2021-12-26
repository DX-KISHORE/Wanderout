import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

query ="""CREATE TABLE students(id int NOT NULL AUTO_INCREMENT,uname varchar(50) NOT NULL,uname varchar(50) NOT NULL, age int NOT NULL, PRIMARY KEY (id))"""

cur.execute(query)