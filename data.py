import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

q ="""CREATE TABLE data(id int(5) AUTO_INCREMENT PRIMARY KEY,name varchar(50) NOT NULL,gender varchar(6),department varchar(6),password varchar(6))"""
cur.execute(q)