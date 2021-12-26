#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

q="""select * from data """
cur.execute(q)

r=cur.fetchall()

print("""
<html>
<body>
<i><center><h1>Welcome Admin</h1></center><i>

    <button><a href="student_home.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Home</a></button>
    <button><a href="student_details.py"style="text-decoration:none;font-size:12pt;font-weight:bold;" >Student details</a></button>
    <button><a href="stud_mark details.py" style="text-decoration:none;font-size:12pt;font-weight:bold;" >Student Marks</a></button>
    <button><a href="update_mark.py" style="text-decoration:none;font-size:12pt;font-weight:bold;" >Update Marks</a></button>
    <button><a href="student_login.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Logout</a></button><hr>
    
<center>
    <h2><i>Student Details</i></h2>
    <table cellspacing="0" cellpadding="15" border="5">
    <tr>
        <th>id</th> 
        <th>name</th> 
        <th>gender</th> 
        <th>department</th> 
        <th>rollno</th> 
        <th>Add mark</th>
        <th>Delete</th>
        
    </tr>
""")
count=0
for i in r:
    count=count+1
    print("""
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><a href="students_mark.py?rno=%s">Add</a></td>
        <td><a href="delete_mark.py?rno=%s">Delete</a></td>
        
    </tr>
    """%(count,i[1],i[2],i[3],i[5],i[5],i[5]))

print("""
</table>
</center>
</body>
</html>
""")