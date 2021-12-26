import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()

fname = "Kishore"
lname = "kumar"
age= 20

q ="""insert into students(fname,lname,age) values('%s','%s','%s')"""%(fname,lname,age)

cur.execute(q)
conn.commit()

conn.close()
