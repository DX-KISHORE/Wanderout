#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

q = """select max(id) from reg"""
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

rno = "WOUT" + z + str(n + 1)



print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
    <title>Wanderout</title>
    <link rel="stylesheet" href="style1.css">
</head>
<body>


        <div class="navbar">
            <div>
                <a href='website.html'>WANDER OUT</a>
            </div>
            <nav>
                <ul id='MenuItems'>
                    <li><a href='home.py'>Home</a></li>
                    <li><a href='places'>Places</a></li>
                    <li><a href='mybooking.py'>My status</a></li>
                     <li><a href='review.py'>Reviews</a></li>
                    <li><a href='contact.py'>Contact</a></li>
                    <li><button class='loginbtn' onclick="location.href='login.py';">Login</button></li>
                </ul>
            </nav>
        </div>

    <div class="full-page">
        <div class="center">
      <h1>Signup</h1>
      <form method="post">
        <div class="text">
          <input type="text" id="fname" name="fname" placeholder="Full name" onchange="document.getElementById('drno').value= this.value+document.getElementById('rno').value;" required />
        </div>
        <div class="text">
          <input type="text" id="email" name="email" placeholder="Email address" required>
        </div>
        <div class="text">
          <input type="password" id="pass" name="pass" placeholder="Password" required>
        </div>
        <input type="hidden" id="rno" value="%s">
        <div class="text">
            Customer Id:
             <input type="text" name="drno" id="drno" readonly/>
        </div>
        
        <input type="submit" class="submit" id="sub" name="sub" value="Signup">
        
        
      </form>
    </div>

   <div class="footer">
        <div class="box-container">
            <div class="box">
                <h3>About us</h3>
                <p>Have you Bored being in a Same Place? Want to make ADVENTURE ???</p>
            </div>
            <div class="box">
                <h3>Branch locations</h3>
                <a href="#">India</a>
                <a href="#">USA</a>
                <a href="#">Japan</a>
                <a href="#">France</a>
            </div>
            <div class="box">
                <h3>Quick links</h3>
                <a href="home.py">Home</a>
                <a href="places.py">Places</a>
                <a href="package.py">Package</a>
                <a href="services.py">Services</a>
                <a href="review.py">Review</a>
                <a href="contact.py">Contact</a>
            </div>
            <div class="box">
                <h3>Follow us</h3>
                <a href="#">facebook</a>
                <a href="#">instagram</a>
                <a href="#">twitter</a>
                <a href="#">linkedin</a>
            </div>
        </div>
            <h1 class="credit"> created by <span> KMS TEAM </span> | all rights reserved! </h1>
   </div>
   </div>




</body>  
</html>
"""%(rno))

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

f = cgi.FieldStorage()
sub = f.getvalue("sub")
fullname = f.getvalue("fname")
email = f.getvalue("email")
password = f.getvalue("pass")
drno = f.getvalue("drno")

if sub != None:
    q = """insert into customer(fullname,email,password,coustid) values('%s','%s','%s','%s')""" %(fullname,email,password,drno)
    cur.execute(q)
    conn.commit()
    print("""
    <script>
    alert("Account created successfully")
    location.href="login.py";
    </script>
    """)
    conn.close()
