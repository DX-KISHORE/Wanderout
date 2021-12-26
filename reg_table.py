import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

q ="""CREATE TABLE travel(id int(20) AUTO_INCREMENT PRIMARY KEY,idno varchar(100) NOT NULL,fullname varchar(50) NOT NULL,age varchar(30) NOT NULL,
gender varchar(50) NOT NULL,phonenumber varchar(50) NOT NULL,location varchar(50) NOT NULL,
fromdate varchar(50) NOT NULL,todate varchar(50) NOT NULL,person varchar(50) NOT NULL,address varchar(50) NOT NULL,
city varchar(50) NOT NULL,state varchar(50) NOT NULL,pincode varchar(10000) NOT NULL)"""
cur.execute(q)
conn.commit()
conn.close()