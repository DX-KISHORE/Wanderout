#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi,pymysql,cgitb
cgitb.enable()

f = cgi.FieldStorage()
rno = f.getvalue("rno")

#print(rno)

print("""
<html>
<head>
</head>
<body>
<i><center><h1 class="header">Welcome Admin</h1></center><i>
  
    <button><a href="student_home.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Home</a></button>
    <button><a href="student_details.py"style="text-decoration:none;font-size:12pt;font-weight:bold;">Student details</a></button>
    <button><a href="stud_mark details.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Student Marks</a></button>
    <button><a href="update_mark.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Update Marks</a></button>
    <button><a href="student_login.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Logout</a></button><hr>
    
    <center>
    <form action= "#" method="post" autocomplete="off">
               <h1>Delete the selected student %s</h1>
                <input type="submit" value="Delete" name="sub" onclick="location.href='stud_mark details.py';"/>
               <input type="button" name="button" value="Cancel" onclick="Location.href='student_details.py';"/>
    </form>           
    </center>
"""%(rno))

sub= f.getvalue('sub')
if sub!=None:

    conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
    cur = conn.cursor()

    q = """DELETE from data where rollno='%s'"""%rno
    cur.execute(q)

    q1 = """DELETE from mark where rollno='%s'""" % rno
    cur.execute(q1)

    conn.commit()
    print("""
        <script>
        alert("Deleted sucessfully");
        location.href("student_details.py");
        </script>
    """)
    conn.close()
print("""
</body>
</html>
""")