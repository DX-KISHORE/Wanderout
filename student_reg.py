#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb, os, smtplib
cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

q="""select max(id) from data"""
cur.execute(q)

r=cur.fetchone()
if r[0]!=None:
    n=r[0]
else:
    n=0

if n < 9:
    z = "000"
elif n < 99:
    z = "00"
elif n < 999:
    z = "0"
else:
    z = ""

rno = "abc" + z + str(n + 1)



print("""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<body>
<center>
<form action="student_reg.py" method="post" autocomplete="off" enctype="multipart/form-data style="background-color:black;width:500px;color:white;">
    <h3>Signup</h3>
    Name<input type="text" name="uname" placeholder="Enter your name" required/><br><br>
    <input type="hidden" id="rno" value="%s">
    Gender<br>
    Male<input type="radio" id="male" name="gender" value="Male">
    Female<input type="radio" id="female" name="gender" value="female"><br><br>
    Department<select name="dept" id="dept" onchange="document.getElementById('drno').value= this.value+document.getElementById('rno').value;" required />
        <option default>Department</option>
        <option default>IT</option>
        <option default>CSE</option>
        <option default>EEE</option>
        <option default>MECH</option>
    </select><br><br>
    Password:<input type="password"  placeholder="password here" name="pass" required/><br><br>
    <b>rollno:</b><input type="text" name="drno" id="drno" readonly/><br><br>
    <input type="submit" value="Submit" name="sub" onclick="location.href='student_login.py';"/>
    <input type="button" value="Cancel" onclick="location.href='student_reg.py';"/>


</form>
</center>
</body>
</html>
"""%(rno))

f = cgi.FieldStorage()
sub = f.getvalue("sub")
name = f.getvalue("uname")
gender = f.getvalue("gender")
department = f.getvalue("dept")
password = f.getvalue("pass")
drno = f.getvalue("drno")
# print(f)

if sub != None:
    q = """insert into data(name,gender,department,password,rollno) values('%s','%s','%s','%s','%s')""" %(name, gender, department, password, drno)
    cur.execute(q)
    conn.commit()
    print("""
    <script>
    alert("Account created successfully")
    location.href="student_login.py";
    </script>
    """)
    conn.close()