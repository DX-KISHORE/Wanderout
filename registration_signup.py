#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb, os, smtplib
cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

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
<form action="registration_signup.py" method="post" autocomplete="off" enctype="multipart/form-data style="background-color:black;width:500px;color:white;">
    
    <h2><i>PERSONAL INFORMATION</i></h2> 
    Name:
    <input type="text" id="uname" name="uname"  placeholder="Enter your name" required /><br><br>
    Gender:
    <input type="radio" id="gender" name="gender" value="male"  required />Male
    <input type="radio" id="gender" name="gender" value="Female" required />female<br><br>
    DOB:
    <input type="date" id="dob" name="dob" required /><br><br>
    Age:
    <input type="number" id="age" name="age" min="1"max="100" required /><br><br>
    Phone number:
    <input type="tel" id="phno" name="phno" required /><br><br>
    District:
         <select name="district" id="district">
           <option id="Madurai" >Madurai</option>
           <option id="Thirchy">Thirchy</option>
           <option id="Coimbatore" >Coimbatore</option>
           <option id="Chennai" >Chennai</option>
           <option id="Other" >Other</option>
         </select><br><br>
    State:
    <input list="state" name="state">
         <datalist id="state">
           <option value="Tamilnadu">
           <option value="Maharastra">
           <option value="Kerala">
           <option value="Dehli">
           <option value="Other">
         </datalist><br><br>
    Email ID:
    <input type="email" id="emailid" name="emailid"  placeholder="ABC@gmail.com" required /><br><br>
    Password:
    <input type="password" id="pass" name="pass" required /><br><br>
    <input type="submit" value="Submit" name="sub" onclick="location.href='registration_login.py';"/>
    <input type="button" value="Cancel" onclick="location.href='registration_signup.py';"/>
</form>        
</center>
</body>
</html>
""")

f = cgi.FieldStorage()
sub = f.getvalue("sub")
name = f.getvalue("uname")
gender = f.getvalue("gender")
dob = f.getvalue("dob")
age = f.getvalue("age")
phonenumber = f.getvalue("phno")
district = f.getvalue("district")
state = f.getvalue("state")
emailid =f.getvalue("emailid")
password = f.getvalue("pass")

print(f)

if sub != None:
    q = """insert into personaldata(name,gender,dob,age,phonenumber,district,state,emailid,password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
        %(name,gender,dob,age,phonenumber,district,state,emailid,password)
    cur.execute(q)
    conn.commit()
    print("""
    <script>
    alert("Account created successfully")
    location.href("registration_login.py")
    </script>
    """)
    conn.close()