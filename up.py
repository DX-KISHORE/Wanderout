#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

f = cgi.FieldStorage()
rno = f.getvalue('')

print("""
<html>
<head>
</head>
<body>


 <i><center><h1>Update Mark</h1></center></i>
    <button><a href="student_home.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Home</a></button>
    <button><a href="student_details.py"style="text-decoration:none;font-size:12pt;font-weight:bold;">Student details</a></button>
    <button><a href="stud_mark details.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Student Marks</a></button>
    <button><a href="update_mark.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Update Marks</a></button>
    <button><a href="student_login.py" style="text-decoration:none;font-size:12pt;font-weight:bold;">Logout</a></button><hr>

<center>
<form action="#" method="post" autocomplete="off" enctype="multipart/form-data style="background-color:black;width:500px;color:white">

    Exam:
         <select name="exam" id="exam" required/>
           <option>Internal exam</option>
           <option>Revision exam</option>
           <option>Semester exam</option>
           <option>Aptitude exam</option>
           <option>Other</option>
         </select><br><br>

    Tamil:
        <input type="number" name="tam" id="tam" min="1"max="100" required/><br><br>    
    English:
        <input type="number" name="eng" id="eng" min="1"max="100" required/><br><br>    
    Maths:
        <input type="number" name="mat" id="mat" min="1"max="100" required/><br><br>
    Science:
        <input type="number" name="sci" id="sci" min="1"max="100" required/><br><br>
    Social:
        <input type="number" name="soc" id="soc" min="1"max="100" required/><br><br>

    <input type="submit" value="Update" name="sub">
    <input type="button" value="Cancel" onclick="location.href='update_mark.py;"/>
</form>
</center>
</body>
</html>

""")

sub = f.getvalue("sub")

if sub != None:
    Exam = f.getvalue("exam")
    Tamil = int(f.getvalue("tam"))
    English = int(f.getvalue("eng"))
    Maths = int(f.getvalue("mat"))
    Science = int(f.getvalue("sci"))
    Social = int(f.getvalue("soc"))
    Total = Tamil + English + Maths + Science + Social
    Average = (Tamil + English + Maths + Science + Social) / 5
    # print(f)

    conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
    cur = conn.cursor()

    q = """UPDATE mark SET exam='%s',Tamil='%s',English='%s',Maths='%s',Science='%s',Social='%s',Total='%s',Average='%s' where rollno='%s'""" % (
    Exam, Tamil, English, Maths, Science, Social, Total, Average, rno)
    cur.execute(q)
    conn.commit()
    print("""
       <script>
       alert("Mark updated");
       location.href='update_mark.py';
       </script>
       """)
    conn.close()



