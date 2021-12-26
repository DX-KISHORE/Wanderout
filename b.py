import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

q ="""CREATE TABLE travel(id int(5) AUTO_INCREMENT PRIMARY KEY,idno varchar(100) NOT NULL,fullname varchar(50) NOT NULL,
age int(50) NOT NULL,gender varchar(50) NOT NULL,phonenumber int(50) NOT NULL,location varchar(50) NOT NULL,
fromdate varchar(50) NOT NULL,todate varchar(50) NOT NULL,person int(50) NOT NULL,
address varchar(50) NOT NULL,city varchar(50) NOT NULL,state varchar(50) NOT NULL,pincode double(699999) NOT NULL)"""
cur.execute(q)