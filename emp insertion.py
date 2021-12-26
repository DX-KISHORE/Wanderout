import cgi,pymysql,cgitb
cgitb.enable()
conn = pymysql.connect(host="localhost",user="root",password="",database="julybatch")
cur = conn.cursor()
n = int(input("enter the number of rows you want to insert"))

for i in range(0,n):
    name = str(input("Enter name of %s employment"%(i+1)))
    gender = str(input("Enter gender of %s employment"%(i+1)))
    age = int(input("Enter age of %s employment"%(i+1)))
    salary = int(input("Enter salary of %s employment" % (i + 1)))

    q ="""insert into employment(name,gender,age,salary) values('%s','%s','%s','%s')"""%(name,gender,age,salary)
    cur.execute(q)
conn.commit()
conn.close()
