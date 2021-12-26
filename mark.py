import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

q ="""CREATE TABLE mark(id int(10) AUTO_INCREMENT PRIMARY KEY,rollno varchar(30) NOT NULL,exam varchar(6)NOT NULL,
Tamil int(5)NOT NULL,English int(5)NOT NULL,Maths int(5)NOT NULL,Science int(5)NOT NULL,Social int(5)NOT NULL,Total int(20)NOT NULL,
Average int(20)NOT NULL)"""
cur.execute(q)
conn.commit()
conn.close()