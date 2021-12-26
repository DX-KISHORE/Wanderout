#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi,pymysql,cgitb
cgitb.enable()
f = cgi.FieldStorage()
rno = f.getvalue("rno")


print("""
<html>
<body>
<i><center><h1>Welcome Admin</h1></center><i>

    <button><a href="student_home.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Home</a></button>
    <button><a href="student_details.py"style="text-decoration:none;font-size:12pt;font-weight:bold;" >Student details</a></button>
    <button><a href="student_marks.py" style="text-decoration:none;font-size:12pt;font-weight:bold;" >Student Marks</a></button>
    <button><a href="admin_login.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Logout</a></button><hr>
</body>
</html>
""")