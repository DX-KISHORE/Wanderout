#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

q = """select * from mark """
cur.execute(q)

r = cur.fetchall()

print("""
<html>
<body>
<i><center><h1>student mark</h1></center><i>
    <button><a href="student_home.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Home</a></button>
    <button><a href="student_details.py"style="text-decoration:none;font-size:12pt;font-weight:bold;" >Student details</a></button>
    <button><a href="stud_mark details.py" style="text-decoration:none;font-size:12pt;font-weight:bold;" >Student Marks</a></button>
    <button><a href="update_mark.py?rno=%s" style="text-decoration:none;font-size:12pt;font-weight:bold;" >Update Marks</a></button>
    <button><a href="student_login.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Logout</a></button><hr>
    
<center>
 
    <table cellspacing="0" cellpadding="15" border="5">
    <tr>
        <th>id</th> 
        <th>Rollno</th> 
        <th>Exam</th> 
        <th>Tamil</th> 
        <th>English</th> 
        <th>Maths</th>
        <th>Science</th>
        <th>Social</th>
        <th>Total</th>
        <th>Average</th>
    </tr>
""")
count = 0
for i in r:
    count = count + 1
    print("""
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
    """ % (count, i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

print("""
</table>
</center>
</body>
</html>
""")