#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi,pymysql,cgitb
cgitb.enable()


print("""
<html>
    <head>
    <title>Registartion form</title>
    </head>
        <body>
            <center><h2><i>Registration Form</i></h2>
            <form action="#" method="post" autocomplete="off">
                <input type="text" name="uname" placeholder="Email address" required/><br><br>
                <input type="password" name="pwd" placeholder="Password" required/><br><br>
                <input type="submit" name="sub" value="Login" onclick="location.href='registration.py';"/>
                <input type="button" value="Cancel" onclick="location.href='registration_login.py';"/>
                <input type="button" value="Signup" onclick="location.href='registration_signup.py';"/>
            </form>
            </center>
        </body>
</html>
""")

f=cgi.FieldStorage()
uname=f.getvalue("uname")
pwd=f.getvalue("pwd")
sub=f.getvalue("sub")
#print(f)

if sub!=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
    cur = conn.cursor()
    #print("connected to db")
    q ="""select * from personaldata where emailid='%s' and password='%s'"""%(uname,pwd)
    cur.execute(q)
    #print("data fetched from table")
    r=cur.fetchone()
    if r!=None:
        print("""<script>location.href='registration.py';</script>""")
    else:
        print("""
            <script>
            alert("Invalid username or password..");
            </script>
            """)
    conn.close()
