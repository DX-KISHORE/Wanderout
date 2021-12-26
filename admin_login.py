#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

print("""
<html>
	<head>
		<title>Admin login</title>
		<link href="styles/style1.css" type="text/css" rel="stylesheet"/>
    <link href="styles/images/bg.png" type="text/ico" rel="icon"/>
	</head>
	<body>
			<center><h2><i>Admin login</i></h2>
			<form action="#" method="post" autocomplete="off">
					<input type="text" name="uname" placeholder="Username" required/><br><br>
                    <input type="password" name="pwd" placeholder="Password" required/><br><br>
					<input type="submit" name="sub" value="Login"/>
					<input type="button" value="Cancel" onclick="location.href='admin_login.py';"/>
			</form>
			</center>
	</body>
</html>
""")
import cgi,pymysql,cgitb
f=cgi.FieldStorage()
uname=f.getvalue("uname")
pwd=f.getvalue("pwd")
sub=f.getvalue("sub")
if sub!=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
    cur = conn.cursor()
    q1="""select * from admin where id='%s' and password='%s'"""%(uname,pwd)
    cur.execute(q1)
    #cur.fetchall()--->for multiple records
    #cur.fetchone()--->for single record
    r=cur.fetchall()
    #print("r",r) #((1,'admin','admin'),)
    if r != None:
        print("""<script>location.href='student_home.py';</script>""")
    else:
        print("""
        			<script>
        			alert("Invalid username or password..");
        			location.href="admin_login.py";
        			</script>
        			""")
        conn.close()


   