import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

q ="""CREATE TABLE data(id int(5) ,name varchar(50) NOT NULL,gender varchar(50),PRIMARY KEY (id))"""

cur.execute(q)