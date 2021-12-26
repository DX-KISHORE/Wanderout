import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

q ="""CREATE TABLE personaldata(id int(20) AUTO_INCREMENT PRIMARY KEY,name varchar(30) NOT NULL,gender varchar(10) NOT NULL,dob varchar(20) NOT NULL,
age int(5) NOT NULL,phonenumber int(20) NOT NULL,district varchar(30) NOT NULL,state varchar(30) NOT NULL,emailid varchar(30) NOT NULL,
password varchar(30) NOT NULL)"""
cur.execute(q)
conn.commit()
conn.close()