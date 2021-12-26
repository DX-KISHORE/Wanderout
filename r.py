import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

q ="""CREATE TABLE customer(id int(5) AUTO_INCREMENT PRIMARY KEY,fullname varchar(50) NOT NULL,email varchar(50) NOT NULL,password varchar(50) NOT NULL,coustid varchar(50) NOT NULL)"""
cur.execute(q)