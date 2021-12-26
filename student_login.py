#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb
cgitb.enable()




print("""

<html>
    <head>
    <title>student login</title>
    </head>
        <body>
            <center><h2><i>Student login</i></h2>
            <form action="#" method="post" autocomplete="off">
                <input type="text" name="uname" placeholder="Username" required/><br><br>
                <input type="password" name="pwd" placeholder="Password" required/><br><br>
                <input type="submit" name="sub" value="Login"/>
                <input type="button" value="Cancel" onclick="location.href='student_login.py';"/>
                <input type="button" value="Signup" onclick="location.href='student_reg.py';"/>
            </form>
            </center>
        </body>
</html>
""")

f=cgi.FieldStorage()
rno=f.getvalue("uname")
pwd=f.getvalue("pwd")
sub=f.getvalue("sub")
#print(f)

if sub!=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
    cur = conn.cursor()
    #print("connected to db")
    q ="""select * from data where rollno='%s' and password='%s'"""%(rno,pwd)
    cur.execute(q)
    #print("data fetched from table")
    r=cur.fetchone()
    if r!=None:

        print("""
        <script>
            location.href="student_home.py?rno=%s";
        </script>
        """%(rno))
    else:
        print("""
            <script>
            alert("Invalid username or password..");
            location.href="student_login.py";
            </script>
            """)
    conn.close()
