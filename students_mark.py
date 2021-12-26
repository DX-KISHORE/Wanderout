#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi,pymysql,cgitb
cgitb.enable()

f = cgi.FieldStorage()
rno = f.getvalue("rno")

print("""
<html>
<head>
</head>
<body>
<center>
<i><h1>Students Marks</h1></i>
<form action="students_mark.py?rno=%s" method="post" autocomplete="off" enctype="multipart/form-data style="background-color:black;width:500px;color:white">
    
    
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
    
    <input type="submit" value="Submit" name="sub" onclick="location.href='stud_mark details.py';"/>
    <input type="reset" value="Cancel" onclick="location.href='students_mark.py?rno=%s';"/>


</form>
</center>
</body>
</html>
"""%(rno,rno))



sub = f.getvalue("sub")

if sub != None:

    Exam = f.getvalue("exam")
    Tamil = int(f.getvalue("tam"))
    English = int(f.getvalue("eng"))
    Maths = int(f.getvalue("mat"))
    Science = int(f.getvalue("sci"))
    Social = int(f.getvalue("soc"))
    Total = Tamil+English+Maths+Science+Social
    Average = (Tamil+English+Maths+Science+Social)/5
    #print(f)

    conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
    cur = conn.cursor()

    q="""INSERT INTO mark(rollno,Exam,Tamil,English,Maths,Science,Social,Total,Average) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(rno,Exam,Tamil,English,Maths,Science,Social,Total,Average)
    cur.execute(q)
    conn.commit()
    print("""
       <script>
       alert("Student mark inserted");
       location.href("stud_mark details.py");
       </script>
       """)
    conn.close()


