import cgi,pymysql,cgitb
cgitb.enable()
conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()
n = int(input("enter the number of rows you want to insert"))

for i in range(0,n):
    fname = str(input("Enter fname of %s person"%(i+1)))
    lname = str(input("Enter lname of %s person"%(i+1)))
    age = int(input("Enter age of %s person"%(i+1)))

    q ="""insert into students(fname,lname,age) values('%s','%s','%s')"""%(fname,lname,age)
    cur.execute(q)
conn.commit()
conn.close()
   